from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('newpost/', views.newpost, name ='newpost'),
    path('post/<int:post_id>', views.post, name='post'),
    path('ajax/plus', views.plus, name='plus')
]
