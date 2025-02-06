import requests


class JsonApi:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com/"

    def get_posts(self):
        return requests.get(f"{self.base_url}posts")

    def get_post_number(self, number):
        return requests.get(f"{self.base_url}posts/{number}")

    def post_posts(self, data, headers):
        return requests.post(f"{self.base_url}posts", data=data, headers=headers)

    def put_post(self, number, data, headers):
        return requests.put(
            f"{self.base_url}posts/{number}", data=data, headers=headers
        )
