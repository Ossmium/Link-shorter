from django.urls import path
from .views import index, LinkDeleteView, LinkListView
from link_app import services

urlpatterns = [
    path("", index, name="index"),
    path("urls/delete/<int:pk>/", LinkDeleteView.as_view(), name="url_delete"),
    path("urls/<str:url>", services.redirection, name="url_detail"),
    path("urls/", LinkListView.as_view(), name="urls"),
]
