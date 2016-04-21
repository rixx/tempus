from django.conf.urls import include, url

from .views import (
    results,
    CategoryView,
    CreateCategoryView,
    CreateEntryView,
    CreateProjectView,
    DeleteEntryView,
    DeleteProjectView,
    IndexView,
    ProjectView,
)

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),

    url(r'^results/$', results, name='results'),
    url(r't/new/$', CreateCategoryView.as_view()),
    url(r'^t/(?P<category>[a-zA-Z0-9\-]+)/$', CategoryView.as_view(), name='category'),

    url(r'^t/(?P<category>[a-zA-Z0-9\-]+)/new/$', CreateProjectView.as_view(), name='new_project'),
    url(r'^t/(?P<category>[a-zA-Z0-9\-]+)/(?P<project>[a-zA-Z0-9\-]+)/$', ProjectView.as_view(), name='project'),
    url(r'^t/(?P<category>[a-zA-Z0-9\-]+)/(?P<pk>[a-zA-Z0-9\-]+)/delete$', DeleteProjectView.as_view(), name='delete_project'),

    url(r'^t/(?P<category>[a-zA-Z0-9\-]+)/(?P<project>[a-zA-Z0-9\-]+)/new/$', CreateEntryView.as_view(), name='project'),
    url(r'^t/(?P<category>[a-zA-Z0-9\-]+)/(?P<project>[a-zA-Z0-9\-]+)/(?P<pk>[a-zA-Z0-9\-]+)/delete$', DeleteEntryView.as_view(), name='delete_entry'),

    url(r'^$', IndexView.as_view(), name='index'),
]
