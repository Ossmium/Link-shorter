from .models import Link
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'link_app/index.html')


class DeleteURLView(LoginRequiredMixin, DeleteView):
    model = Link
    success_url = reverse_lazy('accounts:users_urls')

    http_method_names = [
        "post",
    ]

    def post(self, request, *args, **kwargs):
        link = None
        try:
            link = Link.objects.get(**kwargs)
        except Link.DoesNotExist:
            raise ValueError('Данная ссылка не существует')
        if not link in request.user.links.all():
            raise ValueError('Данная ссылка не существует')
        return super().post(request, *args, **kwargs)
