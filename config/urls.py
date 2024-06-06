from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


schema_view = get_schema_view(
   openapi.Info(
      title="Deep",
      default_version='v1',
      description="This is Deep API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="None"),
      license=openapi.License(name="MentorKG License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('positions/', include('apps.positions.urls')),
    path('subjectdetails/', include('apps.subjectDetails.urls')),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)