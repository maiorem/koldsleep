from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin) :
    search_fields = ['title'],

# Register your models here.
admin.site.register(Project, ProjectAdmin)