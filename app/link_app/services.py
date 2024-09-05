from .models import Link
from django.http import HttpResponseRedirect
from django.db.models import F
from django.core.cache import cache


def get_full_url(url):
    if cache.has_key(url):
        Link.objects.filter(short_url=url).update(click_count=F("click_count") + 1)
        return cache.get(url)
    link = Link.objects.filter(short_url=url)
    if link.first():
        link.filter().update(click_count=F("click_count") + 1)
        cache.set(link.first().short_url, link.first().full_url, timeout=300)
        return link.first()
    raise KeyError("Данный URL не существует, попробуйте другой")


def redirection(request, url):
    full_url = get_full_url(url)
    return HttpResponseRedirect(str(full_url))
