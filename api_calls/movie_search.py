"""
Title: movie_search module of the Moview project
Authors: Driss BENSAID & Enzo Fragale
Date of creation: 15/11/2022

"""
import requests
import json
import os
from dotenv import load_dotenv

class MovieSearch:
    """
    Contains various functions to retrieve results from a movie search request
    on the imdb API.
    """
    _searchTitle=""
    _responseMovieSearch=""
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, title):
        """
        Initalises the class instance based on the title of the movie to be
        searched.

        Parameters
        ----------
        title : String
            Represents the title of the movie to be searched.

        Returns
        -------
        None.

        """
        self._searchTitle = title
        load_dotenv()
        apiKey=os.getenv("KEY")
        self._responseMovieSearch = requests.get(
            "https://imdb-api.com/API/SearchMovie/" + apiKey + "/"
            + self._searchTitle)
        
    def __repr__(self) -> str:
        return f"{type(self).__name__}(type={self._type}, \
                message={self._message}, created_at={self._created_at})"
    
    def get_response(self):
        """
        Gets and returns the response of the movie search request of the title
        passed when initialising the class instance on the imdb API as a JSON
        object.
        
        Returns
        -------
        response : String
            The response of the movie search request of the title passed when 
            initialising the class instance on the imdb API as a JSON object.

        """
        response = self._responseMovieSearch.json()
        return response
    
    def get_movies(self):
        """
        Gets and returns all the movie descriptions matching the title passed when
        initialising the class instance as a JSON array.
        
        Returns
        -------
        movies : String
            All the movie descriptions matching the title passed when initialising the
            class instance as a JSON array.

        """
        movies =  self.get_response()["results"]
        return movies
    
    def get_best_match_movie(self):
        """
        Gets and returns the movie description with the best match with the title
        passed when intialising the class instance as a JSON object.

        Returns
        -------
        titles : String
            The movie description with the best match with the title passed when 
            intialising the class instance as a string.

        """
        return self.get_movies()[0]
    
    def get_ids(self):
        """
        Gets and returns all the movie ids matching the title passed when
        intialising the class instance as a list of strings.

        Returns
        -------
        titles : String list
            All the movie ids matching the title passed when initialising
            the class instance as a list of strings.

        """
        movies = self.get_movies()
        ids = [movie["id"] for movie in movies]
        return ids
    
    def get_best_match_id(self):
        """
        Gets and returns the id of the movie with the best match with the title
        passed when intialising the class instance as a string.

        Returns
        -------
        titles : String
            The id of the movie with the best match with the title passed when 
            intialising the class instance as a string.

        """
        return self.get_ids()[0]
