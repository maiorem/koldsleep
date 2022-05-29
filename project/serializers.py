from dataclasses import fields
from rest_framework import serializers, routers, viewsets
from .models import Project

class ProjectSerializer(serializers.HyperlinkedModelSerializer) :
    class Meta :
        model = Project
        fields = ['id', 'title', 'cdate', 'start_time', 'end_time', 'place', 'link', 'tag', 'proceeding', 'poster', 'content', 'isVisible']