from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader

from .models import Task, Tag, Reminder

def index(request):
    template = loader.get_template('endlesstodolist/home.html')
    context = RequestContext(
        request,
        {
            'test_text': "Please Ignore",
        }
    )
    return HttpResponse(template.render(context))
