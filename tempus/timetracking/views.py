from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Category


def index(request):
    template = loader.get_template('t/index.html')
    context = {'all_categories': Category.objects.all()}
    return HttpResponse(template.render(context, request))

def category(request, category):
    return HttpResponse('This site will show you projects of category {}.'.format(category))

def project(request, category, project):
    return HttpResponse('This site will show you project {} of category {}.'.format(project, category))

def results(request):
    return HttpResponse('Here you will be able to look at your past working habits.')
