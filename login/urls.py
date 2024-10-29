from django.urls import path
from . import views
from django.urls.resolvers import URLPattern


app_name = 'login'
urlpatterns = [
    path('signup/', views.login_superuser, name = 'signup'),
    path('logout/', views.logout, name='logout'),
]

