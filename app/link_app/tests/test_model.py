from django.test import TestCase
from link_app.models import Link


def test_link_create(db, user):
    url = "https://ya.ru"
    count_links = Link.objects.count()
    link = Link(full_url=url, user=user)
    link.save()

    assert link.short_url
    assert Link.objects.count() == count_links + 1
