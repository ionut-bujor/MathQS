from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from createuser.models import user_details
from django.shortcuts import render,redirect
from .models import user, authentication
from createuser.views import hashed_password


def logout(request):
    request.session.flush()
    return render(request,"mainmenu.html")

def get_password_for_username(username):
    try:
        user = user_details.objects.get(username=username)
        return user.password
    except user_details.DoesNotExist:
        return None

def validation_login_user(username, password):
    try:
        user = user_details.objects.get(username=username)

        if get_password_for_username(username) == hashed_password(password):
            return True
        else:
            return False
    except user_details.DoesNotExist:
        return False


user_instance= user()
authentication_instance = authentication()
def login_superuser(request):

    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']

        if get_password_for_username(username) is None:

            authentication_instance.username_found = False

            return render(request,'authentication-login.html',{'authentication_instance':authentication_instance})
        else:
            authentication_instance.username_found = True
        if not validation_login_user(username,password):
            authentication_instance.passwords_match = False

            return render(request,'authentication-login.html',{'authentication_instance':authentication_instance})


        if validation_login_user(username, password):
            authentication_instance.passwords_match = True

            authentication_instance.user_loggedin = True

            request.session['username'] = username
            user_instance.usernameforwritten= username
            return render(request, 'mainmenu.html',{'username_instance':user_instance, 'authentication_instance': authentication_instance})
        else:
            return render(request, "login.html")

    else:
        return render(request, 'login.html')

def getusernameofuser(request):
    if request.method=="POST":
        usernameofuser= request.POST['username']
        return usernameofuser
    
