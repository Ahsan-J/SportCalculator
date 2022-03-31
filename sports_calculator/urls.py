"""sports_calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from team import views as team_views
from match import views as match_views

router = routers.DefaultRouter()
router.register(r'team', team_views.TeamsViewSet, basename='team')
router.register(r'match', match_views.MatchViewSet, basename='match')

urlpatterns = [
    path('', match_views.index),
    path('match/', include('match.urls')),
    path('team/', include('team.urls')),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
