from django.db import models
from django.conf import settings
from pytz import timezone

# Create your models here.
class Board(models.Model) :
    title = models.CharField(max_length=30)
    content = models.TextField()
    writer = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    cdate = models.DateTimeField()

    @property
    def cdate_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.cdate.astimezone(korean_timezone)

    def __str__ (self) :
        return self.title