import uuid
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

WORKOUT_CHOICES = [
    ("Push", "Push"),
    ("Pull", "Pull"),
    ("Leg", "Leg"),
]

MUSCLE_GROUP_CHOICES = [
    ("Shoulders","Shoulders"),
    ("Chest", "Chest"),
    ("Quads", "Quads"),
    ("Biceps", "Biceps"),
    ("Triceps", "Triceps"),
]

EQUIPMENT_CHOICES = [
    ("Free_Weights", "Free Weights"),
    ("Machine", "Machine"),
    ("Cable", "Cable"),
    ("Bodyweight", "Bodyweight"),
]


# class workoutUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     firstName = models.TextField
#     lastName = models.TextField
#     email = models.EmailField
#     homeGym = models.TextField

class Workout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    createdDate = models.DateTimeField(auto_now_add=True)
    focus = models.CharField(max_length=50,choices=WORKOUT_CHOICES, blank=True)
    preworkout = models.BooleanField(default=False)
    totalWeight = models.FloatField(default=0.0)

class Exercise(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    workout = models.ForeignKey(Workout,on_delete=models.CASCADE, editable=False)
    name = models.TextField(blank=True)
    target = models.TextField(blank=True, choices=MUSCLE_GROUP_CHOICES)
    repGoal = models.TextField(blank=True)
    equipment = models.TextField(blank=True, choices=EQUIPMENT_CHOICES)
    notes = models.TextField(blank=True)

class Set(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    exercise = models.ForeignKey(Exercise,on_delete=models.CASCADE, editable=False)
    weight = models.FloatField(default=0.0)
    reps = models.IntegerField(null=True)
    
