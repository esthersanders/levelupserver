"""EventGamer model module"""
from django.db import models


class EventGamers(models.Model):
    """EventGamer database model"""
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="registrations")
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="registrations")
