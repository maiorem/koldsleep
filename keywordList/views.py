from keywordList.models import Keyword
from dream_list.models import Board
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def keylist(request) :
    keyword_list = Keyword.objects.order_by('word')
    return render(request, 'keyword_list/key.html')

def insert_keyword(request) :

    return redirect('keywordList:keylist')   