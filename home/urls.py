# home/urls.py

from django.urls import path
from . import views
from .views import special_offer

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('acinstallation/', views.acinstallation, name='acinstallation'),
    path('antimicrobialfogging/', views.antimicrobialfogging, name='antimicrobialfogging'),
    path('contact/', views.contact, name='contact'),
    path('ductlessminisplits/', views.ductlessminisplits, name='ductlessminisplits'),
    path('MaintenanceandRepair/', views.MaintenanceandRepair, name='MaintenanceandRepair'),
    path('services/', views.services, name='services'),
    path('tuneup/', views.tuneup, name='tuneup'),
    path('special-offer/', views.special_offer, name='special_offer'),
]
