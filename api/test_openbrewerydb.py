import pytest
import requests

BASE_URL = "https://api.openbrewerydb.org/v1/breweries"


@pytest.mark.parametrize("page",
                         [1, 5, 100, 200])
def test_list_breweries(page):
    response = requests.get(f'{BASE_URL}?per_page={page}')
    assert response.status_code == 200, "Expected status code 200"
    new_response = response.json()
    assert len(new_response) == page, f"Expected breweries in the list == {page}"
    assert len(new_response) == page
    for brewery in new_response:
        assert isinstance(brewery, dict), "Each brewery should be a dictionary"
        assert len(brewery) == 16, "Each brewery should have 16 params"
        assert "name" in brewery, "Each brewery should have a name"
        assert "id" in brewery, "Each brewery should have an id"


@pytest.mark.parametrize("city",
                         ["san_diego", "portland", "denver", "shallotte", "rehoboth_beach"])
def test_filter_by_city(city):
    response = requests.get(f'{BASE_URL}?by_city={city}')
    assert response.status_code == 200
    new_response = response.json()
    assert len(new_response) > 0
    for brewery in new_response:
        assert city.replace('_', ' ') in brewery["city"].lower(), f"All breweries should be in {city}"


@pytest.mark.parametrize("country",
                         ["united%20states", "ireland", "france", "south%20korea"])
def test_filter_by_country(country):
    response = requests.get(f'{BASE_URL}?by_country={country}')
    decoded_country = country.replace("%20", " ").lower()
    assert response.status_code == 200, (
        f"Expected status code 200 for country '{decoded_country}', got {response.status_code}"
    )
    new_response = response.json()
    for brewery in new_response:
        assert decoded_country == brewery["country"].lower(), f"All breweries should be in {decoded_country}"
        assert "id" in brewery, "Brewery missing 'id' field"
        assert "name" in brewery, "Brewery missing 'name' field"
        assert len(brewery) == 16, "Each brewery should have 16 params"


@pytest.mark.parametrize("brewery_id",
                         [
                             "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0",
                             "701918b8-49d9-4177-9628-1b6d7d056c06",
                             "1988eb86-f0a2-4674-ba04-02454efa0d31"]
                         )
def test_get_brewery_by_id(brewery_id):
    response = requests.get(f'{BASE_URL}/{brewery_id}')
    assert response.status_code == 200, (
        f"Expected status code 200 for brewery ID '{brewery_id}', got {response.status_code}"
    )
    new_response = response.json()
    for brewery in new_response:
        print(brewery["id"])
        print(brewery_id)
        assert brewery["id"] == brewery_id, (
            f"Expected brewery ID '{brewery_id}', got '{brewery['id']}")
        assert "name" in brewery, "Brewery missing 'name' field"


@pytest.mark.parametrize("brewery_id", [
    "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0",
    "4ffda196-dd59-44a5-9eeb-5f7fd4b58f5a",
    "1988eb86-f0a2-4674-ba04-02454efa0d31"
])
def test_get_brewery_by_id(brewery_id):
    response = requests.get(f'{BASE_URL}/{brewery_id}')
    assert response.status_code == 200, (
        f"Expected status code 200 for brewery ID '{brewery_id}', got {response.status_code}"
    )
    new_response = response.json()
    assert new_response["id"] == brewery_id, (
        f"Expected brewery ID '{brewery_id}', got '{new_response['id']}'"
    )
    assert "name" in new_response, "Brewery missing 'name' field"


def test_get_brewery_by_invalid_id():
    invalid_id = "invalid_abc_id"
    response = requests.get(f'{BASE_URL}/{invalid_id}')
    assert response.status_code == 404, (
        f'Expected status code 404 for invalid ID \'{invalid_id}\', got {response.status_code}'
    )

