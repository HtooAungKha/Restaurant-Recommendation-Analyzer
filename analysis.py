import os
import sqlite3

import matplotlib

# Use a non-interactive backend so Matplotlib works safely with Flask
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


class RestaurantAnalysis:
    def __init__(self, db_path="data/restaurants.db"):
        self.db_path = db_path

    def load_data(self):
        connection = sqlite3.connect(self.db_path)

        dataframe = pd.read_sql_query(
            "SELECT * FROM restaurants",
            connection,
        )

        connection.close()
        return dataframe

    def total_restaurants(self):
        dataframe = self.load_data()
        return len(dataframe)

    def average_rating(self):
        dataframe = self.load_data()

        if dataframe.empty:
            return 0

        return round(dataframe["rating"].mean(), 2)

    def average_reviews(self):
        dataframe = self.load_data()

        if dataframe.empty:
            return 0

        return round(dataframe["review_count"].mean(), 2)

    def highest_rated_restaurant(self):
        dataframe = self.load_data()

        if dataframe.empty:
            return None

        highest_rated = dataframe.sort_values(
            by=["rating", "review_count"],
            ascending=[False, False],
        ).iloc[0]

        return highest_rated

    def average_rating_by_category(self):
        dataframe = self.load_data()

        if dataframe.empty:
            return pd.Series(dtype=float)

        return (
            dataframe.groupby("category")["rating"]
            .mean()
            .sort_values(ascending=False)
        )

    def price_distribution(self):
        dataframe = self.load_data()

        if dataframe.empty:
            return pd.Series(dtype=int)

        cleaned_prices = (
            dataframe["price"]
            .fillna("Not listed")
            .replace("", "Not listed")
        )

        return cleaned_prices.value_counts()

    def top_reviewed_restaurants(self, limit=10):
        dataframe = self.load_data()

        if dataframe.empty:
            return dataframe

        return dataframe.sort_values(
            by="review_count",
            ascending=False,
        ).head(limit)

    def generate_charts(self):
        dataframe = self.load_data()

        if dataframe.empty:
            return False

        chart_folder = "static/charts"
        os.makedirs(chart_folder, exist_ok=True)

        self._create_rating_chart(
            dataframe,
            chart_folder,
        )

        self._create_price_chart(
            dataframe,
            chart_folder,
        )

        self._create_reviews_chart(
            dataframe,
            chart_folder,
        )

        return True

    def _create_rating_chart(self, dataframe, chart_folder):
        rating_data = (
            dataframe.groupby("category")["rating"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
            .sort_values()
        )

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.barh(
            rating_data.index,
            rating_data.values,
        )

        ax.set_title("Average Rating by Category")
        ax.set_xlabel("Average Rating")
        ax.set_ylabel("Category")
        ax.set_xlim(0, 5)

        fig.tight_layout()

        fig.savefig(
            os.path.join(
                chart_folder,
                "rating_by_category.png",
            ),
            dpi=150,
            bbox_inches="tight",
        )

        plt.close(fig)

    def _create_price_chart(self, dataframe, chart_folder):
        price_order = [
            "$",
            "$$",
            "$$$",
            "$$$$",
            "Not listed",
        ]

        price_data = (
            dataframe["price"]
            .fillna("Not listed")
            .replace("", "Not listed")
            .value_counts()
            .reindex(price_order, fill_value=0)
        )

        display_labels = [
            "Budget",
            "Moderate",
            "Expensive",
            "Luxury",
            "Not listed",
    ]

        fig, ax = plt.subplots(figsize=(9, 6))

        positions = list(range(len(price_data)))

        ax.bar(
            positions,
            price_data.values,
        )

        ax.set_title("Restaurant Price Distribution")
        ax.set_xlabel("Price Level")
        ax.set_ylabel("Number of Restaurants")

        ax.set_xticks(positions)
        ax.set_xticklabels(
            display_labels,
            rotation=0,
        )

        fig.tight_layout()

        fig.savefig(
            os.path.join(
                chart_folder,
                "price_distribution.png",
            ),
            dpi=150,
            bbox_inches="tight",
        )

        plt.close(fig)

    def _create_reviews_chart(self, dataframe, chart_folder):
        review_data = (
            dataframe.sort_values(
                by="review_count",
                ascending=False,
            )
            .head(10)
            .sort_values(
                by="review_count",
                ascending=True,
            )
        )

        fig, ax = plt.subplots(figsize=(10, 6))

        ax.barh(
            review_data["name"],
            review_data["review_count"],
        )

        ax.set_title("Top 10 Restaurants by Review Count")
        ax.set_xlabel("Number of Reviews")
        ax.set_ylabel("Restaurant")

        fig.tight_layout()

        fig.savefig(
            os.path.join(
                chart_folder,
                "top_reviewed.png",
            ),
            dpi=150,
            bbox_inches="tight",
        )

        plt.close(fig)