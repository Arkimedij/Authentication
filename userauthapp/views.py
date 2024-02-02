from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User registration successful")         
    else:
        form = UserCreationForm()
        
    return render(request,'register.html',{'form':form})


def login(request):
    
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')