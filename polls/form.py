from django import forms

from .models import Question
from .models import Choice

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question_text','imag')

class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ('choice_text',)