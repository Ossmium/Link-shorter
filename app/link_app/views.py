from .models import Link
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import URLForm


def index(request):
    return render(request, "link_app/index.html")


class LinkListView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    login_url = "/login/"
    form_class = URLForm
    template_name = "link_app/urls_list.html"
    success_url = reverse_lazy("link_app:urls")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["urls"] = Link.objects.all()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class LinkDeleteView(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = reverse_lazy("accounts:users_urls")

    http_method_names = [
        "post",
    ]

    def post(self, request, *args, **kwargs):
        if not (request.user.is_staff or request.user.is_superuser):
            get_object_or_404(request.user.links.all(), **kwargs)
        return super().post(request, *args, **kwargs)
