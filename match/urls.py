from django.urls import path, include
from match import views

urlpatterns = [
    path('', views.index),
    path('<id>/', views.renderMatchById),
]