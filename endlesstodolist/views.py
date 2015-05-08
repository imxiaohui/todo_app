from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate, login

from .models import Task, Tag, Reminder
from .forms import LoginForm

def index(request):
    if request.user.is_authenticated():
        return render(request, 'endlesstodolist/home.html')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                # Authenticate
                user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password']
                )
                if user is not None and user.is_active:
                    # Log the user in.
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                else:
                    form = LoginForm()
                    return render(request, 'endlesstodolist/login.html', {
                        'form': form,
                        'message': "Login Error"
                    })

        else:
            form = LoginForm()
            return render(request, 'endlesstodolist/login.html', {
                'form': form
            })

def home(request):
    pass
