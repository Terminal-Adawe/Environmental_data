from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import redirect

from analytics.models import ComplianceValue

from  analytics.forms import loginForm
from  analytics.forms import indexloginForm
from  analytics.forms import registerForm

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=username,password=password)

                if user is not None:
                    auth_login(request, user)
                    user = User.objects.get(username=username)

                    if user.is_staff == 1:
                        return HttpResponseRedirect('/analytics/dashboard')
                    else:
                        return HttpResponseRedirect('/dataProcessor/')
                else:
                    return HttpResponseRedirect('login')
    else:
        form = loginForm()
        return render(request, 'analytics/landingpage/index.html',{'form': form})

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'analytics/dashboard/dashboard.html')
    else:
        return HttpResponseRedirect('login')

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)

        if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user = authenticate(username=username,password=password)

                if user is not None:
                    auth_login(request, user)
                    user = User.objects.get(username=username)

                    if user.is_staff == 1:
                        return HttpResponseRedirect('/analytics/dashboard')
                    else:
                        return HttpResponseRedirect('/dataProcessor/')
                else:
                    return HttpResponseRedirect('login')
    else:
        form = loginForm()
        return render(request, 'analytics/login/login.html', {'form': form})
	

def registerUser(request):
    if request.method == 'POST':
        form = registerForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            if  password != password_confirm:
                 return render(request, 'analytics/login/register.html', {
                    'form': form,
                    'error_message': ' Passwords do not match '
                })

            else:
                user = User.objects.create_user(username, email, password)
                user.last_name = lastname
                user.first_name = firstname
                user.save()

                return HttpResponseRedirect('register_user')
    else:
        form = registerForm()
        return render(request, 'analytics/login/register.html',{'form': form})

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('login')

def media(request):
    if request.user.is_authenticated:
        return render(request, 'analytics/dashboard/media.html')
    else:
        return HttpResponseRedirect('login')