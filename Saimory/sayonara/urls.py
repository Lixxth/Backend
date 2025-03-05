from django.contrib import admin
from django.urls import path
from sayonara.views import index

urlpatterns = [
    path('',index),
]
