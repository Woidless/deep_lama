from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PositionsListView.as_view(), name='positions-list'),
    path('create/', views.PositionCreateView.as_view(), name='positions-create'),
    path('update/<int:pk>', views.PositionUpdateView.as_view(), name='positions-update'),
    path('delete/<int:pk>', views.PositionDeleteView.as_view(), name='positions-delete'),
]