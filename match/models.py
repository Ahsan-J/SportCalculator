from django.db import models
from team.models import Team

# Create your models here.
class Match(models.Model):
    id = models.CharField(max_length=126, primary_key=True)
    team_one = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="team_one", blank=True, null=True)
    team_two = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="team_two", blank=True, null=True)
    team_one_score = models.IntegerField(default=0)
    team_two_score = models.IntegerField(default=0)
    winner = models.ForeignKey(Team, on_delete=models.DO_NOTHING, related_name="winner", blank=True, null=True)
    match_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Match of " + self.team_one.name + " vs " + self.team_two.name
