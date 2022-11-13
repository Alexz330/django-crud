from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError


def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:

        if request.POST['password1'] == request.POST['password2']:

            try:

                username = request.POST["username"]
                password = request.POST["password1"]
                user = User.objects.create_user(
                    username=username, password=password)
                user.save()
                login(request=request, user=user)
                return redirect('tasks')

            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, "error": "user already exists"})

        return render(request, 'signup.html', {'form': UserCreationForm, "error": "password do not match"})


def tasks(request):
    return render(request, 'tasks.html')


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):

    if request.method == "GET":
        return render(request, 'signin.html', {
            "form": AuthenticationForm

        })
    else:
        print(request.POST)
        user = authenticate(
            request=request,
            username=request.POST['username'],
            password=request.POST['password']
        )

        if user is None:
            print("no encontrado")
            return render(request, 'signin.html',{
                'form':AuthenticationForm,
                'error':"Username or password is incorrect"
           
            })
        else:
            login(request=request,user=user)
            return redirect('tasks')
