from api import YelpAPI
from database import RestaurantDatabase


def main():
    api = YelpAPI()
    database = RestaurantDatabase()

    location = input("Enter a location: ").strip()
    keyword = input("What would you like to find? ").strip()

    limit_input = input("How many results? (Press Enter for 30): ").strip()

    if limit_input == "":
        limit = 30
    else:
        try:
            limit = int(limit_input)
        except ValueError:
            print("Invalid number. Using the default of 30.")
            limit = 30

    restaurants = api.search_restaurants(
        location=location,
        keyword=keyword,
        limit=limit,
    )

    if not restaurants:
        print("No restaurants were found.")
        return

    database.clear_database()
    database.save_restaurants(restaurants)

    print(f"\nResults for '{keyword}' near {location}\n")

    for restaurant in restaurants:
        print(restaurant)
        print(f"Category: {restaurant.category}")
        print(f"Address: {restaurant.address}")
        print("-" * 50)

    print("\nRestaurants were saved to data/restaurants.db")


if __name__ == "__main__":
    main()