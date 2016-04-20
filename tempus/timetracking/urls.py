from django.conf.urls import url

from .views import (
    results,
    CategoryView,
    CreateEntryView,
    CreateProjectView,
    DeleteEntryView,
    DeleteProjectView,
    IndexView,
    ProjectView,
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),

    url(r'^results/$', results, name='results'),
    url(r'^(?P<category>[a-zA-Z0-9\-]+)/$', CategoryView.as_view(), name='category'),

    url(r'^(?P<category>[a-zA-Z0-9\-]+)/new/$', CreateProjectView.as_view(), name='new_project'),
    url(r'^(?P<category>[a-zA-Z0-9\-]+)/(?P<project>[a-zA-Z0-9\-]+)/$', ProjectView.as_view(), name='project'),
    url(r'^(?P<category>[a-zA-Z0-9\-]+)/(?P<pk>[a-zA-Z0-9\-]+)/delete$', DeleteProjectView.as_view(), name='delete_project'),

    url(r'^(?P<category>[a-zA-Z0-9\-]+)/(?P<project>[a-zA-Z0-9\-]+)/new/$', CreateEntryView.as_view(), name='project'),
    url(r'^(?P<category>[a-zA-Z0-9\-]+)/(?P<project>[a-zA-Z0-9\-]+)/(?P<pk>[a-zA-Z0-9\-]+)/delete$', DeleteEntryView.as_view(), name='delete_entry'),

]
