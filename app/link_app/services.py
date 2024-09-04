from .models import Link
from django.http import HttpResponseRedirect
from django.db.models import F
from django.core.cache import cache


def get_full_url(url):
    if cache.has_key(url):
        Link.objects.filter(short_url=url).update(click_count=F("click_count") + 1)
        return cache.get(url)
    elif link := Link.objects.filter(short_url=url):
        link.filter().update(click_count=F("click_count") + 1)
        cache.set(link[0].short_url, link[0].full_url, timeout=300)
        return link[0]
    raise KeyError("Данный URL не существует, попробуйте другой")


def redirection(request, url):
    full_url = get_full_url(url)
    return HttpResponseRedirect(str(full_url))
