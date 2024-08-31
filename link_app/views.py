from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import URLForm


class IndexView(FormView):
    form_class = URLForm
    template_name = 'index.html'
