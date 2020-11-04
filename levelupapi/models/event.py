"""Event model module"""
from django.db import models



class Event(models.Model):
    """Event database model"""

    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=500)
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="event_game")