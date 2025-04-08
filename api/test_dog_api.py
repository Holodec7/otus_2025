import pytest
from services import dogapi


def test_get_all_breeds_list(dogs_api_client):
    response = dogs_api_client.get_all_breeds_list()
    assert response.status_code == 200
    new_response = response.json()
    assert len(new_response["message"]) > 0
    assert new_response["status"] == "success"


@pytest.mark.parametrize("count",
                         [0, 1, 5, 10])
def test_get_rand_images(dogs_api_client, count):
    response = dogs_api_client.get_rand_images(count)
    assert response.ok
    new_response = response.json()
    if count > 2:
        isinstance(new_response["message"], list)
        assert len(new_response["message"]) == count
    else:
        isinstance(new_response["message"], str)


@pytest.mark.parametrize("breed", ["beagle", "borzoi", "bouvier",  "labrador",
])
def test_get_breed_images_list(dogs_api_client, breed):
    response = dogs_api_client.get_breed_images_list(breed)
    assert response.ok
    new_response = response.json()
    assert len(new_response["message"]) > 0
    assert new_response["status"] == "success"


@pytest.mark.parametrize("breed", ["collie", "buhund", "greyhound",  "pointer",
])
def test_get_sub_breads_list(dogs_api_client, breed):
    response = dogs_api_client.get_sub_breads_list(breed)
    assert response.ok
    new_response = response.json()
    isinstance(new_response["message"], list)
    assert new_response["status"] == "success"


@pytest.mark.parametrize("breed, sub", [("collie", "border" ),
 ("greyhound", "indian"), ("greyhound", "italian"),
 ("hound", "afghan")
])
def test_get_sub_breed_all_images(dogs_api_client, breed, sub):
    response = dogs_api_client.get_sub_breed_all_images(breed, sub)
    assert response.ok
    new_response = response.json()
    isinstance(new_response["message"], list)
    assert len(new_response["message"]) > 0
    assert new_response["status"] == "success"


@pytest.mark.parametrize("breed, sub, count", [("collie", "border", 3),
                                        ("greyhound", "indian", 2), ("greyhound", "italian", 10),
                                        ("hound", "afghan", 10)
                                        ])
def test_get_sub_bread_rand_images(dogs_api_client, breed, sub, count):
    response = dogs_api_client.get_sub_bread_rand_images(breed,sub, count)
    assert response.ok
    new_response = response.json()
    assert len(new_response["message"]) > 0
