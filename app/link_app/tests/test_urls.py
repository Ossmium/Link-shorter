from http import HTTPStatus
from django.urls import reverse


def test_get_index(client):
    response = client.get(reverse("link_app:index"))
    assert response.status_code == 200


def test_redirect(db, link, client):
    response = client.get(
        reverse("link_app:url_detail", kwargs={"url": link.short_url})
    )
    assert response.status_code == HTTPStatus.FOUND
