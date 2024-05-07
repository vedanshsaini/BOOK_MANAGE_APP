from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('add-book/', views.add_book, name='add_book'),
    path('reading-lists/', views.ReadingListListView.as_view(), name='reading_list_list'),
    path('reading-lists/<int:pk>/add/', views.add_book_to_list, name='add_book_to_list'),
    path('reading-lists/<int:list_pk>/remove/<int:book_pk>/', views.remove_book_from_list, name='remove_book_from_list'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLoginView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
]