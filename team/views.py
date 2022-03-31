from django.shortcuts import render
from django.http import HttpResponse
from team.models import Team
from team.serializers import TeamSerializer
from rest_framework import viewsets
# Create your views here.

def index(request):
    context = {
        'teams': Team.objects.order_by('name'),
    }
    return render(request, 'team/index.html', context=context)

def renderTeamById(request, id):
    context = {

    }
    return render(request,'team/detail.html', context=context)

class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.order_by('name')
    serializer_class = TeamSerializer

