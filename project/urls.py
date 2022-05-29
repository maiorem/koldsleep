from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path('api_project_list_info/', views.project, name='project'),
    path('api_project_list_info/<int:id>/', views.projectDetail, name='project_detail'),
]