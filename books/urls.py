from django.urls import path
from . import views

app_name = 'books'


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('(?P<book_id>[0-9]+)/', views.detail, name='detail'),
    path('(?P<book_id>[0-9]+)/delete/', views.delete, name='delete'),
    path('create_book/', views.create_book, name='create-book'),
    path('(?P<book_id>[0-9]+)/book/', views.book, name='book'),
    path('(?P<book_id>[0-9]+)/favorite/', views.favorite, name='favorite'),
    path('favorites/', views.favorites, name='favorites'),
]
