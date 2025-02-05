import pytest
from dog_ceo.dog_api import DogApi

dog_api = DogApi()

list_breed_should_be = ["affenpinscher", "australian", "basenji"]
list_sub_breed = ["australian", "hound"]


@pytest.mark.parametrize("breed", list_breed_should_be)
def test_all_breeds(breed):
    response = dog_api.get_all_breeds()
    assert response.status_code == 200, (
        f"status not 200, current status: {response.status_code}"
    )
    assert "message" in response.json(), "'message' key should by in json"
    assert "status" in response.json(), "'status' key should by in json"
    assert breed in response.json()["message"], f"{breed} should by in json"
    assert "kelpie" in response.json()["message"]["australian"], (
        "'kelpie' should by in json"
    )


def test_random_image():
    response = dog_api.get_random_image()
    assert response.status_code == 200, (
        f"status not 200, current status: {response.status_code}"
    )
    assert response.json()["status"] == "success"


@pytest.mark.parametrize("breed", list_breed_should_be)
def test_by_breed(breed):
    response = dog_api.get_by_breed(breed)
    assert response.json()["status"] == "success"
    assert "https://images.dog.ceo/breeds/" in response.json()["message"][0]
    print("\n", response.json()["message"][0])


@pytest.mark.parametrize("sub_breed", list_sub_breed)
def test_by_sub_breed(sub_breed):
    response = dog_api.get_by_sub_breed(sub_breed)
    print(response.json())
    assert response.json()["status"] == "success"
    assert isinstance(response.json()["message"], list)
    print("\n", response.json()["message"])


def test_browse_breed_list_positive():
    response = dog_api.get_browse_breed_list("akita")
    assert response.status_code == 200, (
        f"status not 200, current status: {response.status_code}"
    )
    assert response.json()["status"] == "success", (
        f"incorrect status: {response.json()['status']}"
    )


def test_browse_breed_list_negative():
    response = dog_api.get_browse_breed_list("not extisting breed")
    assert response.status_code != 200, (
        f"status should be not 200, current status: {response.status_code}"
    )
    assert response.json()["status"] == "error", (
        f"incorrect status: {response.json()['status']}"
    )
