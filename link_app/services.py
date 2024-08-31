from .models import Link
from django.conf import settings
from django.http import HttpResponseRedirect
from django.db.models import F


def get_full_url(url):
    if link := Link.objects.filter(short_url=url):
        link.filter().update(click_count=F('click_count') + 1)
        return link[0]
    raise KeyError('Данный URL не существует, попробуйте другой')


def redirection(request, url):
    full_url = get_full_url(url)
    return HttpResponseRedirect(str(full_url))
