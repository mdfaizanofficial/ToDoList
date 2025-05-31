from django.urls import path
from .views import *

urlpatterns = [
    path('', ListToDo.as_view()),
    path('<int:pk>/', DetailsToDo.as_view()),
    path('create', CreateToDo.as_view()),
    path('delete/<int:pk>', DeleteToDo.as_view())
]