import json
from django.shortcuts import render, redirect, get_object_or_404
from .form import ProjectForm
from .models import Project
from .serializers import ProjectSerializer
from django.core.paginator import Paginator
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.
# 프로젝트 업로드
@csrf_exempt
def projectUpload(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid :
            
            title = request.POST['title']
            start_time = request.POST['start_time']
            end_time = request.POST['end_time']
            place = request.POST['place']
            link = request.POST['link']
            
            tag = request.POST['tag']
            proceeding = request.POST['proceeding']
            content = request.POST['content']
            poster = request.FILES["imgfile"]
            
            fileupload = Project(
                title=title,
                start_time=start_time,
                end_time=end_time,
                place=place,
                link=link,
                tag=tag,
                proceeding=proceeding,
                content=content,
                poster=poster,
            )
            
            fileupload.save()
            return redirect('intro:index')
    else:
        fileuploadForm = ProjectForm()
        context = {
            'form': fileuploadForm,
        }
        return render(request, 'project_form/fileupload.html', context)

# 프로젝트 카드 리스트 (api)
@csrf_exempt
def project(request) :
    project_card = Project.objects.filter(isVisible='true').order_by('-cdate')
    serializer = ProjectSerializer(project_card, many=True)
    return JsonResponse(serializer.data, safe=False)

# 프로젝트 상세보기 (api)
@csrf_exempt
def projectDetail(request, id) :
    project = Project.objects.get(id=id)
    # project.start_time = project.start_time.strftime('%Y년 %m월 %d일')
    # project.end_time = project.end_time.strftime('%Y년 %m월 %d일')
    serializer = ProjectSerializer(project)
    return JsonResponse(serializer.data, safe=False)