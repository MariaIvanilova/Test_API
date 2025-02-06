from dataclasses import dataclass


@dataclass
class BreweryData:
    id_: str
    name: str
    brewery_type: str
    address_1: str
    address_2: str
    address_3: str
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: str
    latitude: str
    phone: str
    website_url: str
    state: str
    street: str

    @staticmethod
    def from_json(json) -> "BreweryData":
        return BreweryData(
            id_=json["id"],
            name=json["name"],
            brewery_type=json["brewery_type"],
            address_1=json["address_1"],
            address_2=json["address_2"],
            address_3=json["address_3"],
            city=json["city"],
            state_province=json["state_province"],
            postal_code=json["postal_code"],
            country=json["country"],
            longitude=json["longitude"],
            latitude=json["longitude"],
            phone=json["phone"],
            website_url=json["website_url"],
            state=json["state"],
            street=json["street"],
        )
