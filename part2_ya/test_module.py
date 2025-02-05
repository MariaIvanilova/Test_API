import requests


def test_main(url, status_code):
    response = requests.get(url=url)
    assert response.status_code == status_code
