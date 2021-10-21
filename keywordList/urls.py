from django.urls import path
from . import views

app_name = 'keywordList'

urlpatterns = [
    path('', views.keylist, name='keylist')

]
