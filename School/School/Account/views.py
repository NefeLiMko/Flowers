from django.shortcuts import render, HttpResponse
from rest_framework import decorators, response
from .models import *
from .serializers import *
# Create your views here.

@decorators.api_view(['GET'])
def materialsView(request):
    if request.method == 'GET':
        queryset = Materials.objects.all()
        serializer = MaterialsSerializer(queryset, many=True)
        print(queryset)
        return response.Response(serializer.data)    

    