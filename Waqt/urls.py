from django.urls import pathfrom . import viewsurlpatterns = [    path('', views.NamazTimesViews),    path('', views.home, name='home'),]