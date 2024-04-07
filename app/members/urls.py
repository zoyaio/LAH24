from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('events/', views.events, name="events"),
    path('eureka/', views.eureka, name="eureka")
]