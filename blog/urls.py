from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('blogwall', views.post_list, name='post_list'),
    path('add_blog/',views.temp, name='create_blog'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.user_login, name='login'),
    path('dashboard/',views.user_dashboard, name='dashboard'),
    path('logout/',views.user_logout, name='logout'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
<<<<<<< HEAD
    path('achieviement/',views.achievement_log, name='achieve'),
=======
>>>>>>> 5c6558eaefe3f0943313e5aeb94b35dd5925aa12
    ]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)