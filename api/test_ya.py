import pytest
import requests


def test_func(url, status_code):
    response = requests.get(url=url)
    assert response.status_code == int(status_code)
