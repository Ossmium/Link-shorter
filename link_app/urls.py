from django.urls import path
from .views import IndexView, ListCreateURLView, DeleteURLView
from link_app import services

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('users/', ListCreateURLView.as_view(), name='users_list'),
    path('users/create/', ListCreateURLView.as_view(), name='users_list'),
    path('urls/', ListCreateURLView.as_view(), name='urls_list'),
    path('urls/<str:url>', services.redirection, name='url_detail'),
    path('urls/delete/<int:pk>/', DeleteURLView.as_view(), name='url_delete'),
]
