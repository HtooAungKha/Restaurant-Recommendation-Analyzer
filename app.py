from flask import Flask, render_template, request

from api import YelpAPI
from database import RestaurantDatabase
from analysis import RestaurantAnalysis

app = Flask(__name__)

api = YelpAPI()
database = RestaurantDatabase()
analysis = RestaurantAnalysis()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        location = request.form.get("location", "").strip()
        keyword = request.form.get("keyword", "").strip()
        limit_text = request.form.get("limit", "30").strip()

        if not location:
            return render_template(
                "index.html",
                error="Please enter a location."
            )

        try:
            limit = int(limit_text)
        except ValueError:
            limit = 30

        if limit < 1:
            limit = 1
        elif limit > 50:
            limit = 50

        restaurants = api.search_restaurants(
            location=location,
            keyword=keyword,
            limit=limit,
        )

        if not restaurants:
            return render_template(
                "index.html",
                error="No restaurants were found."
            )

        database.save_restaurants(restaurants)

        return render_template(
            "results.html",
            restaurants=restaurants,
            location=location,
            keyword=keyword,
        )

    return render_template("index.html")

@app.route("/statistics")
def statistics():
    total_restaurants = analysis.total_restaurants()
    average_rating = analysis.average_rating()
    average_reviews = analysis.average_reviews()
    highest_rated = analysis.highest_rated_restaurant()
    charts_created = analysis.generate_charts()

    return render_template(
        "statistics.html",
        total_restaurants=total_restaurants,
        average_rating=average_rating,
        average_reviews=average_reviews,
        highest_rated=highest_rated,
        charts_created=charts_created,
    )

if __name__ == "__main__":
    app.run(debug=True)