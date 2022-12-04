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
    _searchedTitle=""
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
        self._searchedTitle = title
        load_dotenv()
        apiKey=os.getenv("KEY")
        self._responseMovieSearch = requests.get(
            "https://imdb-api.com/API/SearchMovie/" + apiKey + "/"
            + self._searchedTitle)
        
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
    
    def get_descriptions(self):
        """
        Gets and returns all the movie descriptions matching the title passed when
        initialising the class instance as a list of dicts of Strings.
        
        Returns
        -------
        movies : List of Dicts of Strings
            All the movie descriptions matching the title passed when initialising the
            class instance as a list of dicts of Strings.

        """
        descriptions =  self.get_response()["results"]
        return descriptions
    
    def get_best_match_description(self):
        """
        Gets and returns the movie description with the best match with the title
        passed when intialising the class instance as a dict of Strings.

        Returns
        -------
        movie_description : Dict of Strings
            The movie description with the best match with the title passed when 
            intialising the class instance as a dict of Strings.

        """
        movieDescription = self.get_descriptions()[0]
        return movieDescription
    
    def get_ids(self):
        """
        Gets and returns all the movie ids matching the title passed when
        intialising the class instance as a list of strings.

        Returns
        -------
        titles : List of Strings
            All the movie ids matching the title passed when initialising
            the class instance as a list of strings.

        """
        movies = self.get_descriptions()
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
