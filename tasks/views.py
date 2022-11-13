from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse 
def home(request):
    return render(request,'home.html')

def signup(request):
    dic = {'form': UserCreationForm}

    if request.method == 'GET':
        return render(request,'signup.html',dic)
    else:

        if request.POST['password1'] == request.POST['password']:
            try:
                username =  request.POST["username"]
                password =  request.POST["password"]
                user = User.objects.create_user(username=username,password=password)
                user.save()
            except:
                return HttpResponse('Username already exists')
            return HttpResponse('Usuario created successfully')
        return HttpResponse('Password do not match')