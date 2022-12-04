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
    """
    Contains various functions to retrieve ratings from a movie id on the imdb
    API.
    """
    _id=""
    _responseRatings=""
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, id):
        """
        Initalises the class instance based on the id of the movie whose
        ratings need to be retrieved.

        Parameters
        ----------
        id : String
            Represents the id of the movie whose ratings need to be retrieved.

        Returns
        -------
        None.

        """
        self._id = id
        load_dotenv()
        apiKey=os.getenv("KEY")
        self._responseRatings = requests.get(
            "https://imdb-api.com/API/Ratings/" + apiKey + "/" 
            + self._id)
        
    def __repr__(self) -> str:
        return f"{type(self).__name__}(type={self._type}, \
            message={self._message}, created_at={self._created_at})"
    
    def get_response(self):
        """
        Gets and returns the response of the ratings retrieval request of the
        id passed when initialising the class instance on the imdb API as a
        JSON object.
        
        Returns
        -------
        response : String
            The response of the ratings retrieval request of the id passed when
            initialising the class instance on the imdb API as a JSON object.
            
        """
        response = self._responseRatings.json()
        return response
    
    def get_ratings_list(self):
        """
        Gets and returns all the ratings on the id passed when intialising the 
        class instance as a list of strings.

        Returns
        -------
        ratingsList : String list
            All the ratings on the id passed when intialising the class
            instance as a list of strings.

        """
        ratings =  self.get_response()
        ratingsList = list(ratings.items())[5:-1]
        return ratingsList
