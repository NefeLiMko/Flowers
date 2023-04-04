from django.db import models
from django.core.validators import MaxValueValidator
from Users.models import Task, Profile
# Create your models here.

# TODO Materials -> Video, Docs
class Materials(models.Model):
    title = models.CharField(max_length=20) # Lesson title
    video = models.FileField(upload_to='uploads/video')
    documentation = models.TextField(max_length=10000)

    def __str__(self):
        return self.title
    
# TODO Exercises -> Theory, Practic
class Exercises(models.Model):
    title = models.CharField(max_length=20) #Exercise number
    theory = models.FileField(upload_to='uploads/docs')
    # practic = Url to vidget  

# TODO HomeWork -> Tasks
class HomeWork(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.DO_NOTHING)
    task = models.OneToOneField(Task, on_delete=models.DO_NOTHING)
    grade = models.PositiveIntegerField(default=None, validators=[MaxValueValidator(10)])

# TODO Performance ->?
class Performance(models.Model):
    pass
# TODO Help -> Zoom, calendar(Teacher, time), QA, save History
# TODO Active Tasks -> after 6 months