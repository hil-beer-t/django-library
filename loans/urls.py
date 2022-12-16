from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/list', views.list_books, name='list')
]