from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin) :
    search_fields = ['title']

# Register your models here.
admin.site.register(Board, BoardAdmin)
