from .models import *
from rest_framework import serializers


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = ['title', 'video', 'documentation']