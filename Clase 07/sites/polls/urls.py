from django.urls import path

from . import views
from .views import questions

urlpatterns = [
    path("", views.index, name="index"),
    path('questions', questions, name='questions'),  # GET API

]