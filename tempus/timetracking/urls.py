from django.conf.urls import url

from .views import (
    results,
    CategoryView,
    CreateProjectView,
    DeleteProjectView,
    IndexView,
    ProjectView,
)

urlpatterns = [
    # /t/
    # shows all categories (work/fun/uni) and a quickstart menu
    url(r'^$', IndexView.as_view(), name='index'),

    # /t/results
    url(r'^results/$', results, name='results'),

    # /t/work/
    # shows all projects and entries for a category
    url(r'^(?P<category>[a-zA-Z0-9]+)/$', CategoryView.as_view(), name='category'),

    # /t/work/redo_things
    # shows project redo_things from category work
    url(r'^(?P<category>[a-zA-Z0-9]+)/new/$', CreateProjectView.as_view(), name='new_project'),
    url(r'^(?P<category>[a-zA-Z0-9]+)/(?P<pk>[a-zA-Z0-9]+)/delete$', DeleteProjectView.as_view(), name='delete_project'),
    url(r'^(?P<category>[a-zA-Z0-9]+)/(?P<project>[a-zA-Z0-9]+)/$', ProjectView.as_view(), name='project'),

]
