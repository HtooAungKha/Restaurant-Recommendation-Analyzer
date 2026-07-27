class Restaurant:
    def __init__(self, business_id, name, rating, price, review_count, category, address, yelp_url):
        self.business_id = business_id
        self.name = name
        self.rating = rating
        self.price = price
        self.review_count = review_count
        self.category = category
        self.address = address
        self.yelp_url = yelp_url

    def __str__(self):
        return (
            f"{self.name} | Rating: {self.rating} | "
            f"Price: {self.price} | Reviews: {self.review_count}"
        )