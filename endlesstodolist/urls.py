from django.conf.urls import url
from . import views

urlpatterns = [
    # / -> Home page for site
    url(r'^$', views.index, name='index'),
    # /home/ -> Home page for tasks and control panel
    url(r'^home/$', views.home, name='home'),
    # /logout/ -> Logs the user out and redirects to the main page.
    url(r'^logout/$', views.logout_user, name='logout_user'),
    # /tasks/* -> Task by ID
    url(r'^task/(?P<task_id>[0-9]+)/$', views.task, name='task'),
    # /tags/* -> Tag by name
    url(r'^tag/(?P<tag_name>$)/$', views.tag, name='tag')
]
