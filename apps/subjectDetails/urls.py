from django.urls import path
from .views import SubjectDetailsListView

urlpatterns = [
    path('', SubjectDetailsListView.as_view(), name='subject-details-list'),
]