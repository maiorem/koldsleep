from django.contrib import admin
from .models import Webzine, Blind_Webzine

# Register your models here.
class WebzineAdmin(admin.ModelAdmin) :
    search_fields = ['title']

# Register your models here.
admin.site.register(Webzine, WebzineAdmin)
admin.site.register(Blind_Webzine, WebzineAdmin)