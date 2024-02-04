from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
        
    return render(request,'register.html',{'form':form})


def login(request):
    
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')
    """
    nepal
    hello0099
    """