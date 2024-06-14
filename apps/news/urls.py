from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import news_list, create_news, view_news_detail, edit_news, delete_news

urlpatterns = [
    path('', news_list, name='news_list'),
    path('create/', create_news, name='create_news'),
    path('<int:pk>/', view_news_detail, name='view_news_detail'),
    path('<int:pk>/edit/', edit_news, name='edit_news'),
    path('<int:pk>/delete/', delete_news, name='delete_news'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
