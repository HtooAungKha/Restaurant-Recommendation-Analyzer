import requests

from config import Config
from restaurant import Restaurant


class YelpAPI:
    BASE_URL = "https://api.yelp.com/v3/businesses/search"

    def __init__(self):
        Config.validate()

        self.headers = {
            "Authorization": f"Bearer {Config.YELP_API_KEY}",
            "Accept": "application/json",
        }

    def search_restaurants(self, location, keyword="", limit=30):
        params = {
            "location": location,
            "term": keyword or "restaurants",
            "limit": limit,
        }

        try:
            response = requests.get(
                self.BASE_URL,
                headers=self.headers,
                params=params,
                timeout=10,
            )

            response.raise_for_status()
            data = response.json()

            return self._convert_results(data.get("businesses", []))

        except requests.exceptions.RequestException as error:
            print(f"Yelp API error: {error}")
            return []

    def _convert_results(self, businesses):
        restaurants = []

        for business in businesses:
            categories = business.get("categories", [])

            if categories:
                category = categories[0].get("title", "Unknown")
            else:
                category = "Unknown"

            location = business.get("location", {})
            address_parts = location.get("display_address", [])
            address = ", ".join(address_parts)

            restaurant = Restaurant(
                business_id=business.get("id", ""),
                name=business.get("name", "Unknown"),
                rating=business.get("rating", 0),
                price=business.get("price", "Not listed"),
                review_count=business.get("review_count", 0),
                category=category,
                address=address,
                yelp_url=business.get("url", ""),
            )

            restaurants.append(restaurant)

        return restaurants