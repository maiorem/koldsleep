from dataclasses import fields
from rest_framework import serializers, routers, viewsets
from .models import Project
from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer) :
    tag = TagListSerializerField()
    class Meta :
        model = Project
        fields = '__all__'