from http import HTTPStatus
from django.urls import reverse
from link_app.models import Link


def test_user_can_delete_link(db, user, user_client, link_authored_by_user):
    assert user.links.filter(id=link_authored_by_user.id).exists()

    response = user_client.post(
        reverse(
            "link_app:url_delete",
            kwargs={
                "pk": link_authored_by_user.id,
            },
        ),
        follow=True,
    )

    assert response.status_code == HTTPStatus.OK
    assert not user.links.filter(id=link_authored_by_user.id).exists()


def test_user_cant_delete_else_link(db, link, user_client):
    response = user_client.post(
        reverse(
            "link_app:url_delete",
            kwargs={
                "pk": link.id,
            },
        ),
        follow=True,
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert Link.objects.filter(id=link.id).exists()
