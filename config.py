import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    YELP_API_KEY = os.getenv("YELP_API_KEY")

    @classmethod
    def validate(cls):
        if not cls.YELP_API_KEY:
            raise ValueError(
                "YELP_API_KEY was not found. Add it to your .env file."
            )