from django.shortcuts import render

# Create your views here.

def index(request) :
    return render(request, 'base.html')

def page_not_found(request, exception):
    return render(request, 'common/404.html', {})