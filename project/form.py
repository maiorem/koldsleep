from django import forms
from project.models import Project

class ProjectForm(forms.ModelForm) :
    class Meta :
        model = Project
        fields = ['title', 'start_time', 'end_time', 'place', 'link', 'tag', 'proceeding', 'poster', 'content', ]
        labels = {
            'title' : '프로젝트 제목',
            'content' : '내용',
            'start_time' : '시작 날짜', 
            'end_time' : '끝나는 날짜',
            'place' : '장소', 
            'link' : '신청', 
            'tag' : '태그', 
            'proceeding' : '진행여부', 
            'poster' : '포스터 이미지', 
            'content' : '내용',
        }