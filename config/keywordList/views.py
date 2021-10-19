from django.shortcuts import render

# Create your views here.
def keylist(request) :

    return render(request, 'keyword_list/key.html')   