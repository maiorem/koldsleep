from dream_list.models import Board
from dream_list.form import BoardForm
from keywordList.models import Keyword
from keywordList.insert import KeywordInsert
from collections import Counter
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.core.paginator import Paginator
from konlpy.tag import Mecab



# Create your views here.
def index(request) :
    page = request.GET.get('page', 1) # page 이름으로 넘어오는 정보가 없으면 1
    query=request.GET.get('query')
    # 검색어
    if query :
        dream_list = Board.objects.filter(title__contains=query).order_by('-cdate')
    else :
        dream_list = Board.objects.order_by('-cdate') # 정렬 순서를 cdate decending
    # 페이징 처리
    paginator=Paginator(dream_list, 10) # 페이징 기준을 10개 리스트로
    page_obj=paginator.get_page(page)
       
    context = {'dream_list' : page_obj }
    return render(request, 'dream_list/list.html', context)



def detail(request, id) :
    board = Board.objects.get(id=id)
    context = {'board':board}
    return render(request, 'dream_list/board_detail.html', context)

def board_create(request) :
    mecab = Mecab()
    if request.method=='POST' :
        form=BoardForm(request.POST)
        if form.is_valid() :
            board=form.save(commit=False) # 저장은 하되 커밋은 하지 말 것.
            board.cdate=timezone.now()

            # 키워드 저장
            new_text = request.POST['content']
            print("신규 텍스트 :: ", new_text)
            # 명사 추출
            mecab_nouns = mecab.nouns(new_text)
            
            print("명사 분석 결과 :: ", mecab_nouns)
            # 두 번 이상 쓰여진 키워드만 
            result = Counter(mecab_nouns)
            new_key = []
            for key, value in result.items() :
                if value > 1 :
                    new_key.append(key)
            print("두 번 이상 쓰여진 키워드 :: ", new_key)
            # 한글자 제외        
            new_keywords = [word for word in new_key if len(word) > 1 ]
            all_key = Keyword.objects.all().values_list('word', flat=True) # 데이터베이스 전체 키워드
            all_key = list(all_key)
            print("키워드 목록 ::", new_keywords)
            print("현재까지 저장된 모든 키워드 ::" , all_key)
            # 이미 저장되어 있으면 제외
            if new_keywords not in all_key :
                print("신규 키워드 저장 목록 :: ",new_keywords)
                for keyword in new_keywords :
                    Keyword(word=keyword).save()
            board.save()
            return redirect('dream_list:index')
    else :
        form=BoardForm()
    return render(request, 'dream_list/form.html', {'form':form})


def board_update(request, id) :
    update_board = get_object_or_404(Board, id=id)
    if request.method=='POST' :
        update_form=BoardForm(request.POST, instance=update_board)
        if update_form.is_valid() :
            board=update_form.save(commit=False) 
            board.save()
            return redirect('dream_list:detail', id=id)
        else :
            return redirect('dream_list:index')
    else :
        update_form = BoardForm(instance=update_board)
        return render(request, 'dream_list/update_form.html', {'form':update_form})

def board_delete(request, id) :
    board = get_object_or_404(Board, id=id)
    board.delete()
    return redirect('dream_list:index')