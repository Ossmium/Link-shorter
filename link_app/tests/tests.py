from django.test import TestCase
from link_app.models import Link


def test_link_create():
    url = 'http://ya.ru'
    Link.objects.create(
        url
    )
