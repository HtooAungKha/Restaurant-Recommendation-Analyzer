import sqlite3

class RestaurantDatabase:
    def __init__(self, db_path="data/restaurants.db"):
        self.db_path = db_path
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS restaurants (
                business_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                rating REAL,
                price TEXT,
                review_count INTEGER,
                category TEXT,
                address TEXT,
                yelp_url TEXT
            )
            """
        )

        connection.commit()
        connection.close()

    def save_restaurants(self, restaurants):
        connection = self.connect()
        cursor = connection.cursor()

        for restaurant in restaurants:
            cursor.execute(
                """
                INSERT OR REPLACE INTO restaurants (
                    business_id,
                    name,
                    rating,
                    price,
                    review_count,
                    category,
                    address,
                    yelp_url
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    restaurant.business_id,
                    restaurant.name,
                    restaurant.rating,
                    restaurant.price,
                    restaurant.review_count,
                    restaurant.category,
                    restaurant.address,
                    restaurant.yelp_url,
                ),
            )

        connection.commit()
        connection.close()

    def get_all_restaurants(self):
        connection = self.connect()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                business_id,
                name,
                rating,
                price,
                review_count,
                category,
                address,
                yelp_url
            FROM restaurants
            ORDER BY rating DESC
            """
        )

        restaurants = cursor.fetchall()

        connection.close()

        return restaurants