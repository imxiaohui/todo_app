from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'todo_app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # URL Structure:
    # / -> Front page
    # /tasks/[ID] -> Task by ID
    # /tags/[tag] -> Tag by name
    # /users/[username] -> User by name

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('endlesstodolist.urls')),
]
