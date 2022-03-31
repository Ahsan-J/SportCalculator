from django.shortcuts import render
from match.models import Match
from match.serializers import MatchSerializer
from rest_framework import viewsets
# Create your views here.

def index(request):
    context = {
        'matches': Match.objects.all()
    }
    print(context['matches'])
    return render(request, 'match/index.html', context=context)

def renderMatchById(request, id):
    context = {
        'match': Match.objects.get(id=id)
    }
    return render(request, 'match/detail.html', context=context)

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.order_by('match_date')
    serializer_class = MatchSerializer