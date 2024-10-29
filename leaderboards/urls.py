from django.urls import path 
from . import views 



app_name = 'leaderboards'
urlpatterns = [
    path('leaderboards/', views.show_leaderboard, name = "show_leaderboard")
]