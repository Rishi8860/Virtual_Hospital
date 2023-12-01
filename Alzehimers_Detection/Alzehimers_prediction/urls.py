from django.contrib import admin
from django.urls import path
from Alzehimers_prediction import views

urlpatterns = [
    path('',views.index),
    path('index.html',views.index),
    path('about.html',views.about),
    path('Alzehimer.html',views.Alzehimer)
]
