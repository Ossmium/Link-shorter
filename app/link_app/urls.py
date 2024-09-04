from django.urls import path
from .views import index, DeleteURLView
from link_app import services

urlpatterns = [
    path('', index, name='index'),
    path('urls/<str:url>/', services.redirection, name='url_detail'),
    path('urls/delete/<int:pk>/', DeleteURLView.as_view(), name='url_delete'),
]
