from django.db import models

# Create your models here.
class Comp(models.Model):
    name = models.CharField(max_length=100)
    units = models.TextField()
    team_formation_url = models.TextField()
    core_items = models.TextField()
    gameplan = models.TextField()

    def __str__(self):
        return self.name