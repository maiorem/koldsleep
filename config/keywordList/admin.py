from django.contrib import admin
from .models import Keyword
# Register your models here.


class KeywordAdmin(admin.ModelAdmin) :
    search_fields = ['word']

# Register your models here.
admin.site.register(Keyword, KeywordAdmin)