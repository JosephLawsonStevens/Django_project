from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
def index(request):
    return render(request,'index.html')
def register(request):
    # if request.method == 'POST':
    #     name = request.POST['username']
    #    email = request.POST['email']
    #     if Users.objects.filter(email = email).exists():
    #         messages.info(request,'Email has already used')
    #         return redirect('register')
    #     if Users.objects.filter(name = name).exists():
    #         messages.info(request,'Name has already used')
    #         return redirect('register')
    #     else:
    #         user = Users.objects.create_user(name = name)
    #         user.save()
    #         return redirect('index')
    # else:
    #     return render(request,'login.html')
    #
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account '"  + user +"' has created")
        else:
            return render(request, 'index.html')
    contex = {'form':form}
    return render(request, 'login.html',contex)
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username,password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Input is not correct')
    contex = {}
    return render(request,'login1.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def data(request):
    users = User.objects.all()
    return render(request,'profiles.html',{'users':users})