from django.urls import path, include
from . import views

urlpatterns = [
    path('ana', views.Ana.as_view(), name='ana'),
    path('aab', views.Aab.as_view(), name='aab'),
    path('dkd', views.Dkd.as_view(), name='dkd'),
    path('kgk', views.Kgk.as_view(), name='kgk'),
    path('ktj', views.Ktj.as_view(), name='ktj'),
    path('dk', views.Dk.as_view(), name='dk'),
    path('sbi', views.Sbi.as_view(), name='sbi'),
    path('szs', views.Szs.as_view(), name='szs'),
    path('kgt', views.Kgt.as_view(), name='kgt'),
    path('uksh', views.Uksh.as_view(), name='uksh'),
    path('tzs', views.Tzs.as_view(), name='tzs'),
    path('bjz', views.Bjz.as_view(), name='bjz'),
    path('kjk', views.Kjk.as_view(), name='kjk'),
    path('ata', views.Ata.as_view(), name='ata'),
    path('kna', views.Kna.as_view(), name='kna'),
    path('aash', views.Aash.as_view(), name='aash'),
    path('szr', views.Szr.as_view(), name='szr'),
    path('tjd', views.Tjd.as_view(), name='tjd'),
]