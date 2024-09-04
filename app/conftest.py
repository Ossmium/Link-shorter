import pytest
from link_app.models import Link
from django.test.client import Client
from django.contrib.auth.models import User


@pytest.fixture
def user():
    user = User(username="osmium", password="Test_password123!")
    user.save()
    yield user
    user.delete()


@pytest.fixture
def superuser():
    user = User(username="admin", password="Test_password123!", is_superuser=True)
    user.save()
    yield user
    user.delete()


@pytest.fixture
def link(superuser):
    url = "http://vk.com"
    link = Link(full_url=url, user=superuser)
    link.save()
    yield link

    link.delete()


@pytest.fixture
def link_authored_by_user(user: User, link: Link):
    link.user = user
    link.save()
    yield link


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def user_client(user, client: Client):
    client.force_login(user)
    return client


@pytest.fixture
def superuser_client(superuser, client: Client):
    client.force_login(superuser)
    return client


@pytest.fixture
def links(user):
    admin = User(username="admin", password="Test_password123!")
    admin.save()
    links = [
        Link(full_url="http://ya.ru", user=user),
        Link(full_url="http://vk.com", user=user),
        Link(full_url="http://ya.ru", user=admin),
    ]

    for link in links:
        link.save()

    yield links

    for link in links:
        link.delete()
    admin.delete()
