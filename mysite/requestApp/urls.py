from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *





urlpatterns = [
    path('', CustomLoginView.as_view(), name='home'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('req-list/', ReqList.as_view(), name='req-list'),

    path('req-create/', ReqCreate.as_view(), name='req-create'),
    path('req-update/<int:pk>/', ReqUpdate.as_view(), name='req-update'),

    path('req-delete/<int:pk>/', ReqDelete.as_view(), name='req-delete'),

    path('req-agree/', ReqSign.as_view(), name='req-agree'),

]


