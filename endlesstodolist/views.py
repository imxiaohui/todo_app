from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout

from .models import Task, Tag, Reminder
from .forms import LoginForm

def index(request):
    if not request.user.is_authenticated():
        # Show the login form
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
                    # Show the login form with an error message.
                    form = LoginForm()
                    return render(request, 'endlesstodolist/login.html', {
                        'form': form,
                        'message': "Login Error"
                    })
            else:
                form = LoginForm()
                return render(request, 'endlesstodolist/login.html', {
                    'form': form,
                    'message': "Invalid Login"
                })

        else:
            # Show the login form as normal.
            form = LoginForm()
            return render(request, 'endlesstodolist/login.html', {
                'form': form
            })
    else:
        return render(request, 'endlesstodolist/home.html')

def home(request):
    # TODO: Add live querying of the database so all tasks don't have to be loaded at once.
    if request.user.is_authenticated():
        tasks = Task.objects.all()
        return render(request, 'endlesstodolist/home.html', {
            'tasks': tasks
        })
    else:
        return render(request, 'endlesstodolist/login.html', {
            'message': "You have been logged out"
        })

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def task(request):
    pass

def tag(request):
    pass
