from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Teachers
from django.urls import reverse_lazy

class TeachersListView(ListView):
    model = Teachers
    template_name = 'teachers/teachers-list.html'

class TeachersCreateView(CreateView):
    model = Teachers
    fields = ['first_name', 'middle_name', 'last_name', 'position']
    template_name = 'teachers/teachers-form.html'
    success_url = reverse_lazy('teachers-list')

class TeachersUpdateView(UpdateView):
    model = Teachers
    fields = ['first_name', 'middle_name', 'last_name', 'position']
    template_name = 'teachers/teachers-form.html'
    success_url = reverse_lazy('teachers-list')

class TeachersDeleteView(DeleteView):
    model = Teachers
    template_name = 'teachers/teachers-delete.html'
    success_url = reverse_lazy('teachers-list')