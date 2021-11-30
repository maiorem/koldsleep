from django.urls import path
from . import views

app_name = 'dream_list'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('create/', views.board_create, name='board_create'),
    path('edit/<int:id>/', views.to_edit_form, name='to_edit_form'),
    path('update/<int:id>/', views.board_update, name='board_update'),
    path('delete/<int:id>/', views.board_delete, name="board_delete")
]
