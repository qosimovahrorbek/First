from django.urls import path
from api.views import *

urlpatterns = [
    path('register', Register , name='register'),
    path('login', Login , name='login'),
    path('create-user', CreateUser.as_view()),
    path('create-music', CreateMusic.as_view()),
    path('create-card', CreateCard.as_view()),
    path('delete-card/<int:pk>/', DeleteCard.as_view()),
    path('all-musics/', GetAllMusic.as_view()),
    path('author-musics/<int:pk>/', AuthorMusics.as_view()),
    path('all-users/', AllUsers.as_view()),
]