from django.conf.urls import url

from . import views

urlpatterns = [
    # /time/
    url(r'^$', views.index, name='index'),
    # /time/work/
    url(r'^(?P<category>[a-zA-Z0-9]+)/$', views.projects, name='projects'),
    # /time/overview
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]
