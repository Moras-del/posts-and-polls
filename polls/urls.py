from django.urls import path
from . import views

app_name="polls"

urlpatterns = [
    path('', views.PollsList.as_view(), name='list'),
    path('vote/<int:pk>', views.VoteView.as_view(), name='vote'),
    path('result/<int:poll_id>', views.result, name='result'),
    path('new/', views.CreatePollView.as_view(), name='newpoll'),
]
