from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItecUser
        lookup_field = 'login'
        fields = ['login']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name','surname'] 



class GroupSerializer(serializers.ModelSerializer):
    students = ProfileSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ['name', 'students']

class GradebookSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
       
        read_only=True,
        slug_field='name'
    )
    
    def to_representation(self, instance):
        return f'{instance.group.name}'
    

    
    class Meta:
        model = Gradebook
        fields = ['group'] 




class GradeBookRecordsSerializer(serializers.ModelSerializer):
    pupil = ProfileSerializer(read_only=True)
    gradebook = GradebookSerializer(read_only=True)
 
        
    class Meta:
        model = GradebookRecord
        fields = ['gradebook', 'pupil', 'date', 'grade', 'attendance']
