import pytest
import json
from json_placeholder.json_api import JsonApi


json_api = JsonApi()

headers = {
    "Content-type": "application/json; charset=UTF-8",
}

data_for_post = [
    {
        "title": "test_title_1",
        "body": "test_body_1",
        "userId": 1,
    },
    {"title": "test_title_2", "body": "test_body_3", "userId": 2},
]


def test_get_posts():
    response = json_api.get_posts()
    assert len(response.json()) == 100, "100 posts should be generated"
    assert response.json()[0]["id"] == 1 and response.json()[99]["id"] == 100, (
        "id should be from 1 to 100"
    )


def test_get_posts_contents():
    response = json_api.get_posts()
    flag = True
    i = 0
    for i in range(100):
        if (
            response.json()[i]["userId"] is None
            or response.json()[i]["id"] is None
            or response.json()[i]["title"] is None
            or response.json()[i]["body"] is None
        ):
            flag = False
            break
    assert flag, f"post with id: {i} contains empty elements"


@pytest.mark.parametrize("number", [1, 10, 100])
def test_get_posts_number(number):
    response = json_api.get_post_number(number)
    assert response.json()["id"] == number, f"id should be {number}"


@pytest.mark.parametrize("body", data_for_post)
def test_post_posts(body):
    response = json_api.post_posts(json.dumps(body), headers=headers)
    assert response.status_code == 201, "Status code should by 201 = 'created'"


@pytest.mark.parametrize(
    ["number", "body"],
    [
        (
            1,
            {
                "id": 1,
                "title": "updated_title_1",
                "body": "updated_body_1",
                "userId": 1,
            },
        ),
        (
            10,
            {
                "id": 10,
                "title": "updated_title_2",
                "body": "updated_body_2",
                "userId": 2,
            },
        ),
    ],
)
def test_put_post(number, body):
    response = json_api.put_post(number, json.dumps(body), headers=headers)
    print(f"id: {response.json()['id']} == {number}")
    assert response.status_code == 200, "Status code should by 200 = 'ok'"
    assert response.json()["id"] == number, "id of updated post is incorrect"
