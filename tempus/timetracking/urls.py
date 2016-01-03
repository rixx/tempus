from django.conf.urls import url

from . import views

urlpatterns = [
    # /t/
    # shows all categories (work/fun/uni) and a quickstart menu
    url(r'^$', views.index, name='index'),

    # /t/results
    url(r'^results/$', views.results, name='results'),

    # /t/work/
    # shows all projects and entries for a category
    url(r'^(?P<category>[a-zA-Z0-9]+)/$', views.category, name='category'),

    # /t/work/redo_things
    # shows project redo_things from category work
    url(r'^(?P<category>[a-zA-Z0-9]+)/(?P<project>[a-zA-Z0-9]+)/$', views.project, name='project'),

]