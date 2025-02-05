import requests


class DogApi:
    def __init__(self):
        self.base_url = "https://dog.ceo/api/"

    def get_all_breeds(self):
        return requests.get(f"{self.base_url}breeds/list/all")

    def get_random_image(self):
        return requests.get(f"{self.base_url}breeds/image/random")

    def get_by_breed(self, breed):
        return requests.get(f"{self.base_url}breed/{breed}/images")

    def get_by_sub_breed(self, sub_breed):
        return requests.get(f"{self.base_url}breed/{sub_breed}/list")

    def get_browse_breed_list(self, breed):
        return requests.get(f"{self.base_url}breed/{breed}/images/random")
