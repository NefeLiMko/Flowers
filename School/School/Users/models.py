from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
# Create your models here.

class ItecUser(AbstractUser):

    login = models.CharField(max_length=50)
    REQUIRED_FIELDS = ['login']
    def __str__(self) -> str:
        return self.login



class Group(models.Model):
    name = models.CharField(max_length=40)
    
 
    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    ROLES = [
        ('ST','Student'),
        ('TC','Teacher'),
        ('MG','Manager'),
        ('DR','Director')
    ]
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    second_name = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='')
    user = models.OneToOneField(ItecUser, on_delete=models.CASCADE, primary_key=True) 
    role = models.CharField(max_length=10,choices=ROLES)
    groups = models.ManyToManyField(Group, related_name='students')

    def __str__(self) -> str:
        return self.surname

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    user = models.ManyToManyField(Profile)
    

    def __str__(self) -> str:
        return self.title

class Gradebook(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.group.name

class GradebookRecord(models.Model):
    date = models.DateField(auto_now=True)
    grade = models.PositiveIntegerField(default=None, validators=[MaxValueValidator(10)])
    attendance = models.BooleanField(default=False)
    pupil = models.ForeignKey(Profile, related_name='pupils', on_delete=models.DO_NOTHING)
    gradebook = models.ForeignKey(Gradebook, related_name='gradebooks',  on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.gradebook.group.name}-{self.pupil.surname}-{self.date}'


