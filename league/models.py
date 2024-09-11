from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class DriverProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    race_wins = models.IntegerField(default=0)
    team = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Driver Profile"
        verbose_name_plural = "Driver Profiles"

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def clean(self):
        """Custom validation to prevent negative race_wins."""
        if self.race_wins < 0:
            raise ValidationError("Race wins cannot be negative.")

class RaceResult(models.Model):
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    position = models.IntegerField()
    points = models.IntegerField()
    race_date = models.DateField()

    class Meta:
        ordering = ['-race_date']
        verbose_name = "Race Result"
        verbose_name_plural = "Race Results"

    def __str__(self):
        return f"{self.driver.user.username} - {self.race_date}"

    def clean(self):
        """Ensure position and points are non-negative."""
        if self.position <= 0:
            raise ValidationError("Position must be a positive number.")
        if self.points < 0:
            raise ValidationError("Points cannot be negative.")
