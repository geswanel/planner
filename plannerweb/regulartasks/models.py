from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegularTask(models.Model):
    FREQUENCY_RANGE_CHOICES = (
        ('d', 'days'),
        ('w', 'weeks'),
        ('m', 'months'),
        ('y', 'years')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    last_execution = models.DateTimeField()
    frequency_val = models.PositiveIntegerField()
    frequency_range = models.CharField(max_length=1, choices=FREQUENCY_RANGE_CHOICES)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_id}: {self.title}"
    