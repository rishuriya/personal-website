from django.contrib import admin

from .models import Contact, Post
from .models import Signup
from .models import Achivement

admin.site.register(Post)
admin.site.register(Signup)
admin.site.register(Achivement)
admin.site.register(Contact)
