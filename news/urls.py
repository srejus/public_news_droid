from django.urls import path
from .views import *

urlpatterns = [
    path('post',NewPostView.as_view()),
]