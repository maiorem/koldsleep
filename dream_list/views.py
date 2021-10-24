from dream_list.models import Board
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from dream_list.form import BoardForm
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def index(request) :
    page = request.GET.get('page', 1) # page 이름으로 넘어오는 정보가 없으면 1
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

def edit(request) :
    return render(request, 'dream_list/update_form.html')

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