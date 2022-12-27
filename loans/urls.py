from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='url_home'),
    path('books/list', views.list_books, name='url_list'),
    path('book/create', views.new_book, name='url_new_book'),
    path('book/<int:cod>/loan', views.new_loan, name='url_new_loan'),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
]