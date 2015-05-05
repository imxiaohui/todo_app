from django.conf.urls import url
from . import views

urlpatterns = [
    # / -> Home page for tasks
    url(r'^$', views.index, name='index'),
]
