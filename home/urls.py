from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("mountain", views.mountain, name='mountain'),
    path("beach", views.beach, name='beach'),
    path("desert", views.desert, name='desert'),
    path("Random", views.Random, name='Random'),
    path("contact", views.contact, name='contact'),
]
