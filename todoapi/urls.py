from django.urls import path

from todoapi.views import ToDoList, ToDoDetailView

urlpatterns = [
    path('', ToDoList.as_view()),
    path('<str:id>', ToDoDetailView.as_view())
]