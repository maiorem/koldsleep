from dream_list.models import Board
from django.shortcuts import render, redirect
from django.http import HttpResponse
from dream_list.form import BoardForm
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request) :
    page = request.GET.get('page', 1) # page 이름으로 넘어오는 정보가 없으면 1
    dream_list = Board.objects.order_by('-cdate') # 정렬 순서를 cdate decending
    # 페이징 처리
    paginator=Paginator(dream_list, 10) # 페이징 기준을 5개 리스트로(6개째부터 2페이지)
    page_obj=paginator.get_page(page)
    context = {'dream_list' : page_obj }
    return render(request, 'dream_list/list.html', context)


def detail(request, id) :
    board = Board.objects.get(id=id)
    context = {'board':board}
    return render(request, 'dream_list/board_detail.html', context)

def board_create(request) :
    if request.method=='POST' :
        form=BoardForm(request.POST)
        if form.is_valid() :
            board=form.save(commit=False) # 저장은 하되 커밋은 하지 말 것.
            board.cdate=timezone.now()
            board.save()
            return redirect('dream_list:index')
    else :
        form=BoardForm()
    return render(request, 'dream_list/form.html', {'form':form})


def board_update(request, list_id) :
    update_board = Board.objects.get(id=list_id)
    if request.method=='POST' :
        update_form=BoardForm(request.POST)
        if update_form.is_valid() :
            board=update_form.save(commit=False) 
            board.cdate=timezone.now()
            board.save()
            return redirect('dream_list:detail')
    else :
        update_form = BoardForm(board=update_board, title=request.POST.get('title'), content=request.POST.get('content'), writer=request.POST.get('writer'))
    return render(request, 'dream_list/update_form.html', {'form':update_form})

def board_delete(request, list_id) :
    board = Board.delete(id=list_id)
    return render(request, 'dream_list/list.html')