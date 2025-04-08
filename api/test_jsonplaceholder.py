import pytest
from model import jsonplaceholder


def test_get_posts(placeholder_api_client):
    response = placeholder_api_client.get_posts()
    assert response.ok
    new_response = response.json()
    posts = [jsonplaceholder.Posts.model_validate(obj) for obj in new_response]
    for post in posts:
        assert post.userId > 0
        assert post.id > 0
        assert isinstance(post.title, str)
        assert isinstance(post.body, str)


@pytest.mark.parametrize("id_post",
                        [1, 5, 17, 25],
                        ids=["first_post", "low_id", "medium_id", "high_id"])
def test_get_posts_with_id(placeholder_api_client, id_post):
    response = placeholder_api_client.get_posts_with_id(id_post)
    assert response.ok
    new_response = response.json()
    assert isinstance(new_response, dict)
    assert new_response["id"] == id_post
    jsonplaceholder.Posts.model_validate(new_response)


def test_get_albums(placeholder_api_client):
    response = placeholder_api_client.get_albums()
    assert response.ok
    new_response = response.json()
    albums = [jsonplaceholder.Albums.model_validate(obj) for obj in new_response]
    for album in albums:
        assert album.userId > 0
        assert album.id > 0
        assert isinstance(album.title, str)


@pytest.mark.parametrize("album_id",
                        [1, 5, 17, 25])
def test_get_album(placeholder_api_client, album_id):
    response = placeholder_api_client.get_album(album_id)
    assert response.ok
    new_response = response.json()
    assert isinstance(new_response, dict)
    assert new_response["id"] == album_id
    jsonplaceholder.Albums.model_validate(new_response)


@pytest.mark.parametrize("album, expected_user_id, expected_title", [
    ({"userId": 1, "id": 101, "title": "Test Album1"}, 1, "Test Album1"),
    ({"userId": 3, "id": 101, "title": "Test Album2"}, 3, "Test Album2"),
    ({"userId": 4, "id": 101, "title": "Test Album3"}, 4, "Test Album3"),
    ({"userId": 5, "id": 101, "title": "Test Album4"}, 5, "Test Album4"),
])
def test_create_new_album(placeholder_api_client, album, expected_user_id, expected_title):
    response = placeholder_api_client.create_album(album)
    assert response.ok
    new_response = response.json()
    assert new_response["id"] == 101
    assert new_response["userId"] == expected_user_id
    assert new_response["title"] == expected_title








