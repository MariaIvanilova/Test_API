import requests
from open_brewery_db.models import BreweryData


class BreweryApi:
    def __init__(self):
        self.base_url = "https://api.openbrewerydb.org/v1/breweries"

    def get_list_breweries(self, per_page):
        params = {"per_page": per_page}
        return requests.get(f"{self.base_url}", params=params)

    def get_single_brewery(self, id_):
        return requests.get(f"{self.base_url}/{id_}")

    def get_single_brewery_new(self, id_):
        return BreweryData.from_json(requests.get(f"{self.base_url}/{id_}").json())

    def get_random_brewery(self):
        return requests.get(f"{self.base_url}/random")

    def get_breweries_by_country(self, country):
        params = {"by_country": country}
        return BreweryData.from_json(
            requests.get(f"{self.base_url}", params=params).json()[0]
        )
