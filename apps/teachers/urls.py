from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.TeachersListView.as_view(), name='teachers-list'),
    path('create/', views.TeachersCreateView.as_view(), name='teachers-create'),
    path('update/<int:pk>', views.TeachersUpdateView.as_view(), name='teachers-update'),
    path('delete/<int:pk>', views.TeachersDeleteView.as_view(), name='teachers-delete'),
]