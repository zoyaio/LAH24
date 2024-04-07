from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('events/', views.events, name="events"),
    path('eureka/', views.eureka, name="eureka"),
    path('landing/', views.send_dictionary, name="landing"),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('friends/', views.friends, name='friends'),
    path('pets/', views.pets, name='pets'),


]