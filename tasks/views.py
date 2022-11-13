from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


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
                return HttpResponse('Usuario created successfully')

            except:
                return render(request, 'signup.html', {'form': UserCreationForm, "error": "usernaem already exist"})
        return render(request, 'signup.html', {'form': UserCreationForm, "error": "password do not match"})
