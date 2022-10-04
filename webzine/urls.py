from django.urls import path
from . import views

app_name = "webzine"

urlpatterns = [
    path('api_webzine_list/', views.webzine, name='webzine'),
    path('api_webzine_list/<int:id>/', views.webzineDetail, name='webzine_detail'),
]