from django import forms
from dream_list.models import Board

class BoardForm(forms.ModelForm) :
    class Meta :
        model = Board
        fields = ['cdate', 'title', 'content', 'writer', 'password']
        labels = {
            'cdate' : '날짜',
            'title' : '제목',
            'content' : '내용',
            'writer' : '이름',
            'password' : '비밀번호'
        }