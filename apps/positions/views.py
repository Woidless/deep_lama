from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Positions
from django.urls import reverse_lazy

class PositionsListView(ListView):
    model = Positions
    template_name = 'positions/positions-list.html'

class PositionCreateView(CreateView):
    model = Positions
    fields = ['name']
    template_name = 'positions/positions-form.html'
    success_url = reverse_lazy('positions-list')

class PositionUpdateView(UpdateView):
    model = Positions
    fields = ['name']
    template_name = 'positions/positions-form.html'
    success_url = reverse_lazy('positions-list')

class PositionDeleteView(DeleteView):
    model = Positions
    template_name = 'positions/positions-delete.html'
    success_url = reverse_lazy('positions-list')