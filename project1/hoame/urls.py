from django.urls import path
from . import views

urlpatterns = [
    path('hoame/', views.hoame, name='hoame'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]