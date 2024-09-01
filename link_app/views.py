from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, DeleteView
from .models import Link
from .forms import URLForm


def IndexView(request):
    return render(request, 'link_app/index.html')


class ListCreateURLView(CreateView):
    form_class = URLForm
    template_name = 'link_app/urls_list.html'
    success_url = reverse_lazy('link_app:urls_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context["urls"] = Link.objects.all()
        else:
            context["urls"] = Link.objects.user_links(self.request.user)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteURLView(DeleteView):
    model = Link
    success_url = reverse_lazy('link_app:urls_list')
