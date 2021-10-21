from django.urls import path
from . import views

app_name = 'dream_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('list/create/', views.board_create, name='board_create')
]
