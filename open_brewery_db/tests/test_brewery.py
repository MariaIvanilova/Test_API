import pytest
from open_brewery_db.open_brewery_api import BreweryApi

brewery_api = BreweryApi()


id_correct = "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0"
id_incorrect = "b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e8"

list_country = ["South Korea", "United States"]


@pytest.mark.parametrize("per_page", [1, 3, 5])
def test_list_breweries(per_page):
    response = brewery_api.get_list_breweries(per_page)
    print(f"per page: {per_page} == {len(response.json())}")
    assert len(response.json()) == per_page, (
        "count selected breweries per page is not correct"
    )


@pytest.mark.parametrize(
    ["id_", "is_positive"],
    [(id_correct, True), (id_incorrect, False)],
    ids=["positive test", "negative test"],
)
def test_single_brewery_positive_negative(id_, is_positive):
    response = brewery_api.get_single_brewery(id_)
    if is_positive:
        print(
            f"Positive test. Status code: {response.status_code}, id sent: {id_} == {response.json()['id']} "
        )
        assert response.status_code == 200, "status is not 200"
        assert response.json()["id"] == id_, "id is not the same"
    else:
        print(
            f"Negative test. Status code: {response.status_code}, message: {response.json()['message']}"
        )
        assert response.status_code != 200, "status should not be equal 200"
        assert response.json()["message"] == "Couldn't find Brewery"


def test_single_brewery():
    response = brewery_api.get_single_brewery_new(id_correct)
    print(f"{response.id_} == {id_correct}")
    assert response.id_ == id_correct, "id is not the same"


def test_random_brewery():
    response = brewery_api.get_random_brewery()
    print(f"Count of selected brewery = {len(response.json())}")
    assert response.status_code == 200
    assert len(response.json()) == 1


@pytest.mark.parametrize("country", list_country)
def test_breweries_by_country(country):
    response = brewery_api.get_breweries_by_country(country)
    print(f"Country: {country} == {response.country}")
    assert response.country == country
