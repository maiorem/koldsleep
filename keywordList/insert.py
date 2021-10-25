from django import forms
from keywordList.models import Keyword

class KeywordInsert(forms.ModelForm) :
    class Meta :
        model = Keyword
        fields = ['word']
        labels = {
            'word' : '키워드',
        }