from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Question,Choice
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .form import QuestionForm,ChoiceForm
from django.forms import modelformset_factory

class IndexView(generic.ListView):
    template_name = 'polls/poll_wall.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
def vote(request, question_id):
    print(question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def poll(request):
    if request.session.has_key('_auth_user_id'):
        username=request.user
        choices_formset = modelformset_factory(Choice, form=ChoiceForm, fields=('choice_text',), extra=4)
        if request.method == "POST":
            form=QuestionForm(request.POST,request.FILES)
            choice=choices_formset(request.POST)
            print("hey")
            if form.is_valid() and choice.is_valid():
                post = form.save(commit=False)
                post.pub_date = timezone.now()
                post.assing_to=request.user
                post.save()
                print("well")
                for form in choice:
                    option= form.save(commit=False)
                    option.question = post
                    option.save()
                return redirect('../')
        else:
            form=QuestionForm()
            choice=choices_formset(queryset=Choice.objects.none(),)
        return render(request, 'polls/form.html',{'form': form,'choice':choice,"username":username})
    else:
        return redirect("../login/")