from .models import Blind_Webzine, Webzine
from .serializers import WebzineSerializer, BlindWebzineSerializer
from django.http import JsonResponse
from datetime import datetime


# Create your views here.
# 리스트 (api)
def webzine(request) :
    
    current_time = datetime.now()
    webzine = Blind_Webzine.objects.select_related('webzine_code').order_by('id')  
    
    dict_data = dict()
    idx = 0
    
    for paper in webzine :
        # 오픈 일자가 오늘 날짜보다 이전이거나 같으면 웹진 오픈
        if (paper.webzine_code.open_date <= current_time) :
            title = paper.webzine_code.title
            writer = paper.webzine_code.writer
            writer_info = paper.webzine_code.writer_info
            content = paper.webzine_code.content
            
            list_data = dict()   
            list_data['title'] = title
            list_data['writer'] = writer
            list_data['writer_info'] = writer_info
            list_data['content'] = content
            
            dict_data[idx] = list_data
        
        # 오픈 일자가 오늘 날짜보다 이후면 블라인드   
        else :
            blind_title = paper.blind_title
            blind_writer = paper.blind_writer
            is_blind = paper.is_blind
            blind_list = dict()
            blind_list['title'] = blind_title
            blind_list['writer'] = blind_writer
            blind_list['is_blind'] = is_blind      
            
            dict_data[idx] = blind_list
        
        idx = idx + 1
        
    return JsonResponse(dict_data, safe=False)

# 상세보기 (api)
def webzineDetail(request, id) :
    webzine = Webzine.objects.get(id=id)
    serializer = WebzineSerializer(webzine)
    return JsonResponse(serializer.data, safe=False)