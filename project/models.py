from django.db import models
from django.conf import settings
from pytz import timezone
from taggit.managers import TaggableManager


# Create your models here.
class Project(models.Model) :
    
    # TAG_CHOICES = {
    #   ('공연', '공연'), 
    #   ('전시', '전시'),
    #   ('모임', '모임'),
    #   ('워크숍', '워크숍'),
    #   ('온라인', '온라인'),
    #   ('대관', '대관'),
    #   ('작업', '작업'),
    #   ('기타', '기타')
    # }
    
    PROCEEDING_CHOICES = {
      ('진행중','진행중'), 
      ('마감', '마감'),
      ('진행예정', '진행예정')
    }
    
    title = models.CharField(max_length=50) #프로젝트명
    cdate = models.DateTimeField(auto_now_add=True) #올린 날짜
    
    start_time = models.DateTimeField() #프로젝트 시작 일시
    end_time = models.DateTimeField() #프로젝트 종료 일시
    place = models.CharField(max_length=30) #프로젝트 장소
    link = models.CharField(max_length=30) #프로젝트 신청 링크
    
    tag = TaggableManager(blank=True)
    proceeding = models.CharField(max_length=10, default="진행중", choices=PROCEEDING_CHOICES) #진행 종료 여부
    
    poster = models.ImageField(upload_to="") #포스터 이미지
    content = models.TextField() #프로젝트 내용
    
    isVisible = models.CharField(max_length=10, default='true')

    @property
    def cdate_korean_time(self):
        korean_timezone = timezone(settings.TIME_ZONE)
        return self.cdate.astimezone(korean_timezone)

    def __str__ (self) :
        return self.title