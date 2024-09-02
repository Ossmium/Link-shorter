from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, DeleteView
from .models import Link
from .forms import URLForm


def index(request):
    return render(request, 'link_app/index.html')


class DeleteURLView(DeleteView):
    model = Link
    success_url = reverse_lazy('link_app:urls_list')
