from django.urls import path, include
from team import views

urlpatterns = [
    path('', views.index),
    path('<id>/', views.renderTeamById),
]