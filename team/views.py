from django.shortcuts import render
from django.http import HttpResponse
from team.models import Team
# Create your views here.

def index(request):
    context = {
        'teams': Team.objects.order_by('name'),
    }
    return render(request, 'team/index.html', context=context)