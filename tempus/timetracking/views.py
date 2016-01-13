from django.http import (
    HttpResponse,
    Http404,
)
from django.shortcuts import render
from django.template import loader
from django.views.generic import (
    CreateView, 
    DeleteView,
    ListView,
    View,
)

from .models import (
    Category,
    Entry,
    Project,
)


class IndexView(View):
    template_name = 't/index.html'

    def get(self, request):
        context = {'all_categories': Category.objects.all()}
        return render(request, self.template_name, context)


class CategoryView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 't/category.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        return context

    def get_queryset(self):
        category = Category.objects.get(slug = self.kwargs['category'])
        return category.project_set.all()


class CreateProjectView(CreateView):
    model = Project
    fields = ['name']
    template_name = 't/new_project.html'

    def get_context_data(self, **kwargs):
        context['category'] = self.kwargs['category']
        return context

    def get_success_url(self):
        return '/t/' + self.kwargs['category']

    def form_valid(self, form):
        form.instance.category = Category.objects.get(slug=self.kwargs['category'])
        return super(CreateView, self).form_valid(form)


class DeleteProjectView(DeleteView):
    model = Project
    template_name = 't/delete_project.html'
    
    def get_success_url(self):
        return '/t/' + self.kwargs['category']

class ProjectView(ListView):
    model = Entry
    context_object_name = 'entries'
    template_name = 't/project.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['category'])
        project = category.project_set.get(slug=self.kwargs['project'])
        context['project'] = project
        return context

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['category'])
        project = category.project_set.get(slug=self.kwargs['project'])
        return project.entry_set.all()

class CreateEntryView(CreateView):
    model = Entry
    fields = ['start_time', 'end_time']
    template_name = 't/new_entry.html'

    def get_context_data(self, **kwargs):
        context = super(CreateEntryView, self).get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['category'])
        context['project'] = category.project_set.get(slug=self.kwargs['project'])
        return context

    def get_form(self, form_class):
        form = super(CreateEntryView, self).get_form(form_class)
        form.fields['start_time'].widget.attrs.update({'class': 'datetimepicker'})
        form.fields['end_time'].widget.attrs.update({'class': 'datetimepicker'})
        return form

    def get_success_url(self):
        return '/t/{}/{}'.format(self.kwargs['category'], self.kwargs['project'])

    def form_valid(self, form):
        category = Category.objects.get(slug=self.kwargs['category'])
        form.instance.project = category.project_set.get(slug=self.kwargs['project'])
        return super(CreateView, self).form_valid(form)


class DeleteEntryView(DeleteView):
    model = Entry
    template_name = 't/delete_entry.html'
    
    def get_success_url(self):
        return '/t/{}/{}'.format(self.kwargs['category'], self.kwargs['project'])


def results(request):
    return HttpResponse('Here you will be able to look at your past working habits.')
