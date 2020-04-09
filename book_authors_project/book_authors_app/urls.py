from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('books/<int:number>', views.books),
    path('add_author_to_book', views.add_author_to_book),
    path('author', views.author),
    path('add_author', views.add_author),
    path('author/<int:number2>', views.view_author),
    path('add_book_to_author', views.add_book_to_author),
]