from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('create', views.insert_book, name='insert_book'),
    path('<int:pk>/', views.view_book, name='view_book'),
    path('<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('<int:pk>/delete/', views.delete_book, name='delete_book'),
]