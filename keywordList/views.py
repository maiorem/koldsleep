from keywordList.models import Keyword
from dream_list.models import Board
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def keylist(request) :
    keyword_list = Keyword.objects.order_by('word')
    context = { 'key_list' : keyword_list}
    return render(request, 'keyword_list/key.html', context)


def result(request, word) :

    key_list = Board.objects.filter(content__contains=word).order_by('-id')
    context={'key_list' : key_list}
    return render(request, 'keyword_list/result.html', context)

