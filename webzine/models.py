from datetime import datetime
from django.db import models
from django.conf import settings
from pytz import timezone
from django.utils import timezone

# Create your models here.
class Webzine(models.Model) :
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=10)
    writer_info = models.TextField()
    cdate = models.DateTimeField(default=timezone.now, blank=True)
    open_date = models.DateTimeField()

    @property
    def cdate_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.cdate.astimezone(korean_timezone)

    def __str__ (self) :
        return self.title
    
    
class Blind_Webzine(models.Model) :
    webzine_code = models.ForeignKey(Webzine, related_name='blinds', on_delete=models.SET_NULL, null=True)
    blind_title = models.CharField(max_length=30)
    blind_writer = models.CharField(max_length=10)
    is_blind = models.CharField(max_length=5, default="true", editable=False)
    
    def __str__ (self) :
        return self.blind_title
    
