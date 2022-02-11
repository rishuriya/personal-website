from django import forms

from .models import Signup

class SignupForm(forms.ModelForm):

    class Meta:
        model = Signup
        fields = ('username','email','password', 'cpassword')
        widgets = {
        'password': forms.PasswordInput(),
        'cpassword':forms.PasswordInput()
    }