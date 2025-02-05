from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    description = models.TextField(default="")

    def __str__(self):
        return self.name
    
# one to many

class courseReview(models.Model):
    course = models.ForeignKey(courseType,on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerField()  
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.course.name}'
    
# many to many

class courseStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    course_types = models.ManyToManyField(courseType , related_name="stores")

    def __str__(self):
        return self.name
    
# one to one

class courseInstructor(models.Model):
    course = models.OneToOneField(courseType,on_delete=models.CASCADE, related_name='instructor')
    instructor_name = models.CharField(max_length=100)
    instructor_bio = models.TextField()
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'{self.instructor_name} - {self.course.name}'





