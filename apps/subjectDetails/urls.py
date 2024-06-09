from django.urls import path
from .views import SubjectDetailsListView, DownloadDocxView

urlpatterns = [
    path('', SubjectDetailsListView.as_view(), name='subject-details-list'),
    path('download-docx/', DownloadDocxView.as_view(), name='download-docx'),
]
