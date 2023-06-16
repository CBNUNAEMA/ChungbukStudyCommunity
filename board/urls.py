from .views import *
from django.urls import path

app_name = 'board'

urlpatterns = [
    path('', index, name = 'home'),
    path('post/<str:lectName>', lectBoard, name = 'board'),
    path('post/<str:lectName>/newPost/', NewPost, name='NewPost'),
    path('post/<str:lectName>/see/<int:pk>/', Posting, name ='Posting'),
    path('post/<str:lectName>/question', lectQuest , name = 'Question'),
    path('post/<str:lectName>/info', lectInfo, name = 'Information'),
    path('eval/', evalMain, name='eMain'),
    path('eval/lect/<str:lectName>/<str:professor>', evalBoard, name='eBoard'),
    path('eval/myeval/', myEval, name = 'myEval'),
]