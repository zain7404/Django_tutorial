from django.db import models
from django.utils import timezone

# Create your models here.

class courseType(models.Model):
    COURSE_TYPE_CHOICE = [
        ('BR', 'Beginner'),
        ('IE', 'Intermediate'),
        ('AD', 'Advanced'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=COURSE_TYPE_CHOICE)

    def __str__(self):
        return self.name


