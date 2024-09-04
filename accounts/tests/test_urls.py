from http import HTTPStatus
from django.urls import reverse


def test_get_login(client):
    response = client.get(reverse("accounts:login"))
    assert response.status_code == HTTPStatus.OK


def test_get_signup(client):
    response = client.get(reverse("accounts:signup"))
    assert response.status_code == HTTPStatus.OK


def test_user_cant_get_users_list(db, user_client):
    response = user_client.get(reverse("accounts:users"))
    assert response.status_code == HTTPStatus.FORBIDDEN
