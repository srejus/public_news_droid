from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view()),
    path('<int:id>',IndexView.as_view()),
    path('reporter/',ReporterIndexView.as_view()),

]