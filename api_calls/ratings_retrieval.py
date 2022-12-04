"""
Title: ratings_retrieval module of the Moview project
Authors: Driss BENSAID & Enzo Fragale
Date of creation: 15/11/2022

"""
import requests
import json
import os
from dotenv import load_dotenv

class RatingsRetrieval:
    _id=""
    _responseRatings=""
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, id):
        self._id = id
        load_dotenv()
        apiKey=os.getenv("KEY")
        self._responseRatings = requests.get("https://imdb-api.com/API/Ratings/"
                                                 + apiKey + "/" 
                                                 + self._id)
        
    def __repr__(self) -> str:
        return f"{type(self).__name__}(type={self._type}, message={self._message}, \
                created_at={self._created_at})"
    
    def get_response(self):
        return self._responseRatings.json()
    
    def get_ratings_list(self):
        ratings =  self.get_response()
        ratingsList = list(ratings.items())[5:-1]
        return ratingsList
