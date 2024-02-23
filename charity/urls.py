from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name = "index"),
    path ('about/', views.about, name = "about"),
    path ('contact/', views.contact, name = "contact"),
    path ('blog/', views.blog, name = "blog"),
    path ('donate/', views.donate, name = "donate"),
    path ('appreciation/', views.appreciation, name = "appreciation"),
    path ('fundraiser/', views.fundraiser, name = "fundraiser"),
    path ('support/', views.support, name = "support"),
    path ('gallery/', views.gallery, name = "gallery"),
    path ('terms/', views.terms, name = "terms"),
    path ('faq/', views.faq, name = "faq"),
    ]