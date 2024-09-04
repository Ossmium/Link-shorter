from http import HTTPStatus
from django.urls import reverse
from django.contrib.auth.models import User


def test_user_cant_delete_another_user(db, user_client, superuser):
    response = user_client.post(
        reverse("accounts:users_delete", kwargs={"pk": superuser.id})
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert User.objects.filter(id=superuser.id).exists()


def test_user_cant_create_another_user(db, user_client):
    response = user_client.post(
        reverse("accounts:users_create"),
        data={
            "username": ["test_user"],
            "email": ["popovkd53@gmail.com"],
            "password1": ["MCXIEBa100"],
            "password2": ["MCXIEBa100"],
        },
    )

    assert response.status_code == HTTPStatus.FORBIDDEN
    assert not User.objects.filter(username="test_user").exists()
