from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView, DeleteView
from .forms import URLForm
from .models import Link


class IndexView(FormView):
    form_class = URLForm
    template_name = 'index.html'


class ListCreateURLView(CreateView):
    form_class = URLForm
    template_name = 'urls_list.html'
    success_url = reverse_lazy('link_app:urls_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["urls"] = Link.objects.all()
        return context

    def form_valid(self, form):
        print(self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteURLView(DeleteView):
    success_url = reverse_lazy('link_app:urls_list')
    model = Link
