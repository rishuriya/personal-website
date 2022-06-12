import imp
from operator import mod
from django import forms

from .models import Post
from .models import Achivement
from .models import Contact

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','imag','subtitle', 'text')

class AchivementForm(forms.ModelForm):
    class Meta:
        model = Achivement
        fields=("date","text")

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=("name","email",'subject','message')