from django.shortcuts import render
from django.views import View
from rest_framework import viewsets, permissions, decorators, views
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ItecUser.objects.all().order_by('groups')
    serializer_class = UserSerializer
    lookup_field = 'login'

class GradeBookRecordsViewSet(viewsets.ModelViewSet):
    
    queryset = GradebookRecord.objects.filter()
    serializer_class = GradeBookRecordsSerializer
    

class GradeBookViewSet(viewsets.ViewSet):
    def list(self,request,slug):
        print(slug)
        queryset = GradebookRecord.objects.filter(gradebook=Gradebook.objects.get(group=Group.objects.get(name=slug)))
        print(queryset)
        serializer = GradeBookRecordsSerializer(queryset, many=True)
        return Response(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer     

# TODO Direct Endpoints