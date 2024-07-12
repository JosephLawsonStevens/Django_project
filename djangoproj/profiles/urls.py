from django.urls import  path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('register',views.register,name ='register'),
    path('profiles',views.data,name ='profiles'),
    path('login',views.login_user,name ='login'),
    path('login1',views.logout_user,name ='logout')
]