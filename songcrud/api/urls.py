from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.getAllArtists),
    path('songs/', views.getAllSongs),
    path('songs/<int:pk>/', views.getSong),
    path('songs/add/', views.addSong),
    path('songs/<int:pk>/update', views.updateSong),
    path('songs/<int:pk>/delete/', views.deleteSong)
]