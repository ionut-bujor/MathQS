from django.shortcuts import render
from createuser.models import user_details_quiz
from .models import leaderboards_class

def show_leaderboard(request):
    users_data = user_details_quiz.objects.all()

    leaderboard_dictionary = {}
    for user in users_data:
        username = user.username
        user_points = user.user_points
        leaderboard_dictionary[username] = user_points

    sorted_leaderboard = sorted(leaderboard_dictionary.items(), key=lambda x: x[1], reverse=True)
    leaderboard = leaderboards_class()


    for i in range(0, 5):
        setattr(leaderboard, f"number{i+1}", sorted_leaderboard[i][0])  
        setattr(leaderboard, f"number{i+1}_points", sorted_leaderboard[i][1])  



    return render(request, 'leaderboard.html',{'leaderboard': leaderboard})
