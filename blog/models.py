from distutils.command.upload import upload
import email
<<<<<<< HEAD
from email import message
=======
>>>>>>> 5c6558eaefe3f0943313e5aeb94b35dd5925aa12
from pyexpat import model
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import RegexValidator

class Post(models.Model):
    author= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    imag=models.ImageField(upload_to="images/")
    title = models.CharField(max_length=150)
    subtitle=models.CharField(max_length=300)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Signup(models.Model):
    username=models.CharField(max_length=15,primary_key=True)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=30)
    cpassword=models.CharField(max_length=30)
    def __str__(self):
<<<<<<< HEAD
        return self.username

class Achivement(models.Model):
    date=models.DateField()
    text=models.CharField(max_length=300)

class Contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=50, primary_key=True)
    subject=models.CharField(max_length=400)
    message=models.TextField()
=======
        return self.username
>>>>>>> 5c6558eaefe3f0943313e5aeb94b35dd5925aa12
