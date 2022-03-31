from rest_framework import serializers

from match.models import Match

class MatchSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Match
        fields = ('id', 'team_one', 'team_two', 'team_one_score', 'team_two_score', 'winner')