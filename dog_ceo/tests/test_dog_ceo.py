import pytest
from dog_ceo.dog_api import DogApi

dog_api = DogApi()

list_breed_should_be = ["affenpinscher", "australian", "basenji"]


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
    breed_response = response.json()
    assert breed_response["status"] == "success", "status should by 'success'"
    assert len(breed_response["message"]) > 0, "breed should contain at least 1 image"
    for breed_image in breed_response["message"]:
        assert breed in breed_image, (
            f"expected {breed} should be in image {breed_image}"
        )


@pytest.mark.parametrize(
    "breed, expected_sub_breed",
    [
        ("australian", ("kelpie", "shepherd")),
        (
            "hound",
            ("afghan", "basset", "blood", "english", "ibizan", "plott", "walker"),
        ),
    ],
)
def test_by_sub_breed(breed, expected_sub_breed):
    response = dog_api.get_by_sub_breed(breed)
    sub_breed_data = response.json()
    assert sub_breed_data["status"] == "success", "status should by 'success'"
    assert len(sub_breed_data["message"]) > 0, (
        f"{breed} should contain list of sub_breed"
    )
    assert tuple(sub_breed_data["message"]) == expected_sub_breed, (
        f"incorrect expected sub_breed data for breed {breed}"
    )


def test_browse_breed_list_positive():
    response = dog_api.get_browse_breed_list("akita")
    assert response.status_code == 200, (
        f"status not 200, current status: {response.status_code}"
    )
    assert response.json()["status"] == "success", (
        f"incorrect status: {response.json()['status']}"
    )


def test_browse_breed_list_negative():
    response = dog_api.get_browse_breed_list("not existing breed")
    assert response.status_code != 200, (
        f"status should be not 200, current status: {response.status_code}"
    )
    assert response.json()["status"] == "error", (
        f"incorrect status: {response.json()['status']}"
    )
