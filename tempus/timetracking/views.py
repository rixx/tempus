from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Category


def index(request):
    template = loader.get_template('t/index.html')
    context = {'all_categories': Category.objects.all()}
    return HttpResponse(template.render(context, request))

def category(request, category):
    try:
        category = Category.objects.get(category_name=category)
    except MultipleObjectsReturned:
        return HttpResponse('Whoops, there appear to be multiple categories named "{}". This is really wrong.'.format(category_name))
    except DoesNotExist:
        raise Http404('Category "{}" does not exist.'.format(category.category_name))

    template = loader.get_template('t/category.html')
    context = {'category': category}
    return HttpResponse(template.render(context, request))

def new_project(request, category):
    try:
        category = Category.objects.get(category_name=category)
    except MultipleObjectsReturned:
        return HttpResponse('Whoops, there appear to be multiple categories named "{}". This is really wrong.'.format(category_name))
    except DoesNotExist:
        raise Http404('Category "{}" does not exist.'.format(category.category_name))

    template = loader.get_template('t/new_project.html')
    context = {'category': category}
    return HttpResponse(template.render(context, request))


def project(request, category, project):
    return HttpResponse('This site will show you project {} of category {}.'.format(project, category))

def results(request):
    return HttpResponse('Here you will be able to look at your past working habits.')
