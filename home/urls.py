from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view()),
    path('search',SearchView.as_view()),
    path('<int:id>',IndexView.as_view()),
    path('delete-comment/<int:id>',DeleteCommentView.as_view()),
    path('delete-post/<int:id>',DeletePostView.as_view()),
    path('reporter/',ReporterIndexView.as_view()),

]

