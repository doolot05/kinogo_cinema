from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RegisterForm
from .forms import LoginForm
# Create your views here.

def register(request):
    if request.method == 'GET':
        forms = RegisterForm()
        return render(request, 'users/register.html', {'forms': forms})
    if request.method == 'POST':
        forms = RegisterForm(request.POST)
    if not forms.is_valid():
        return HttpResponse("Error")
    User.objects.create_user(
        username=forms.cleaned_data.get('username'),
        password=forms.cleaned_data.get('password'),
    )
    return redirect("/films/")

def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return HttpResponse("Error")
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
        login(request, user)
    return redirect("/films/")

def logout_user(request):
    logout(request)
    return redirect("/")