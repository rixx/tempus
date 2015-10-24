from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('This site will present you the main categories and your current status.')

def projects(request, category):
    return HttpResponse('This site will show you projects of category {}.'.format(category))

def dashboard(request):
    return HttpResponse('Here you will be able to look at your past working habits.')
