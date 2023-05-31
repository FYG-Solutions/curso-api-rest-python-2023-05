from django.urls import path

from . import views
from .views import questions,  question_detail

urlpatterns = [
    path("", views.index, name="index"),
    path('questions', questions, name='questions'),  # GET API
    path('questions/<int:pk>/', question_detail, name='question_detail'),
]