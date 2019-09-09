from django.urls import path
from . import views

urlpatterns = [
    path('', views.polls,name='polls'),
    path('vote/<poll_id>', views.vote, name='vote'),
    path('result/<int:poll_id>', views.result, name='result'),
    path('new/', views.newpoll, name='newpoll'),
    path('choices/<id>', views.newpollchoices, name='choices'),
]
