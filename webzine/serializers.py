from dataclasses import fields
from rest_framework import serializers, routers, viewsets
from .models import Blind_Webzine, Webzine
     
class WebzineSerializer(serializers.ModelSerializer) :
    blinds = serializers.StringRelatedField(many=True)
    class Meta :
        model = Webzine
        fields = ['title', 'writer', 'writer_info', 'content', 'cdate', 'open_date', 'blinds']  
     
class BlindWebzineSerializer(serializers.ModelSerializer) :
    
    class Meta :
        model = Blind_Webzine
        fields = ['blind_title', 'blind_writer', 'is_blind', 'webzine_code']