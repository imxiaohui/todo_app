from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login

from .models import Task, Tag, Reminder

def index(request):
    context_dict = {}
    template = loader.get_template('endlesstodolist/home.html')
    # If there is any POST data:
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # If we have an active user:
        ## This can later be expanded to show a page when the user's account is inactive.
        if user is not None and user.is_active:
            login(request, user)
            #TODO THIS LINE: get a list of tasks, etc. and put it in context_dict.
            template = loader.get_template('endlesstodolist/user_home.html')
        # If not, show the main page. In the future, this will become an error page.

    return HttpResponse(template.render(RequestContext(request, context_dict))
