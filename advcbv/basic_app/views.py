from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, DeleteView, UpdateView)
from .models import Student, School


class SchoolListView(ListView):

    # context_object_name = 'schools'
    model = School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School  # just returns 'school' by default
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    model = School
    fields = ('name', 'principal', 'location')


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = School


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("basic_app:list")


class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

