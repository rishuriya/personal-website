from django.shortcuts import render
from .models import Achivement, Post
from polls.models import Question,Choice
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .forms import AchivementForm
from .signup import SignupForm
from .forms import ContactForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    question=Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]
    achievements=Achivement.objects.order_by("-date")
    if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                log = form.save(commit=False)
                log.save()
                return redirect('/')
    else:
        form = ContactForm()
    return render(request, 'blog/index.html',{'latest_question_list':question,'posts':posts,'achievements':achievements})

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if post.password==post.cpassword:
                user = User.objects.create_user(post.username, post.email, post.password)
                user.save()
                return redirect("../login")
    else:
        form = SignupForm()
    return render(request, 'blog/signup.html',{'form': form})

def user_login(request):
    print(request.method)
    if request.session.has_key('_auth_user_id'):
        return redirect("../dashboard/")
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print("su")
            if user is not None:
                login(request, user)
                print("hiuh")
                return redirect("../dashboard/")
            else:
                message="Wrong username and Password"
                return render(request, 'blog/login.html',{"message":message})
        return render(request, 'blog/login.html')

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/wall.html', {'posts': posts})
        
def user_dashboard(request):
    print(request.session.keys())
    if request.session.has_key('_auth_user_id'):
        username=request.user
        posts = Post.objects.filter(published_date__lte=timezone.now(), author=username).order_by('published_date')
        return render(request, 'blog/dashboard_profile.html', {'posts': posts,"username":username})
    else:
        return redirect("../login/")

def user_logout(request):
    request.session.flush()
    return redirect("/")

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def temp(request):
    if request.session.has_key('_auth_user_id'):
        username=request.user
        if request.method == "POST":
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                print(post.author)
                return redirect('/')
        else:
            form = PostForm()
        return render(request, 'blog/form.html', {'form': form,"username":username})
    else:
        return redirect("../login/")

def achievement_log(request):
    if request.session.has_key('_auth_user_id'):
        username=request.user
        if request.method == "POST":
            form = AchivementForm(request.POST)
            if form.is_valid():
                log = form.save(commit=False)
                log.save()
                return redirect('/')
        else:
            form = AchivementForm()
        return render(request, 'blog/achievement.html', {'form': form,"username":username})
    else:
        return redirect("../login/")

