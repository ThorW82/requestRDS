from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from .views import *

# app_name = 'req'
urlpatterns = [

    path('', CustomLoginView.as_view(), name='home'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('req-list/', ReqList.as_view(), name='req-list'),

    # path('req-create/', ReqCreate.as_view(), name='req-create'),
    path('req-create/', req_create_view, name='req-create'),

    # path('req-update/<int:pk>/', ReqUpdate.as_view(), name='req-update'),
    path('req-update/<int:id>/', req_update_view, name='req-update'),
    path('req-detail/<int:req_id>/', req_detail_view, name='req-detail'),
    path('req-detail/<int:req_id>/message-create', req_message_add_view, name='message-create'),

    path('req-detail/<int:req_id>/agreed-add', req_agreed_add_view, name='agreed-add'),

    path('req-delete/<int:pk>/', ReqDelete.as_view(), name='req-delete'),
    # path('req-agree/<int:pk>/', ReqSign.as_view(), name='req-agree'),

    # path('message-create/<int:pk>/', MessageCreate.as_view(), name='message-create'),
    path('message-create/', MessageCreate.as_view(), name='message-create'),
]
