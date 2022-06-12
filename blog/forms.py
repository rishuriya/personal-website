<<<<<<< HEAD
import imp
from operator import mod
from django import forms

from .models import Post
from .models import Achivement
from .models import Contact
=======
from django import forms

from .models import Post
>>>>>>> 5c6558eaefe3f0943313e5aeb94b35dd5925aa12

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
<<<<<<< HEAD
        fields = ('title','imag','subtitle', 'text')

class AchivementForm(forms.ModelForm):
    class Meta:
        model = Achivement
        fields=("date","text")

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields=("name","email",'subject','message')
=======
        fields = ('title','imag','subtitle', 'text')
>>>>>>> 5c6558eaefe3f0943313e5aeb94b35dd5925aa12
