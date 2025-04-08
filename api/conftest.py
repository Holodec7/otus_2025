import pytest
from services.dogapi import DogsApiClient
from services.placeholder import PlaceholderApiClient


@pytest.fixture()
def dogs_api_client():
    client = DogsApiClient()
    return client


@pytest.fixture()
def placeholder_api_client():
    client = PlaceholderApiClient()
    return client


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Request url"
    )

    parser.addoption(
        "--status",
        default=200,
        help="Status code",
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status")
