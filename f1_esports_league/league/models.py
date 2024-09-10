from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    race_wins = models.IntegerField(default=0)
    team = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class RaceResult(models.Model):
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    position = models.IntegerField()
    points = models.IntegerField()
    race_date = models.DateField()

    def __str__(self):
        return f"{self.driver.user.username} - {self.race_date}"
