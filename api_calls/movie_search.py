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
    _searchTitle=""
    _responseMovieSearch=""
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, title):
        self._searchTitle = title
        load_dotenv()
        apiKey=os.getenv("KEY")
        self._responseMovieSearch = requests.get("https://imdb-api.com/API/SearchMovie/"
                                                 + apiKey + "/" 
                                                 + self._searchTitle)
        
    def __repr__(self) -> str:
        return f"{type(self).__name__}(type={self._type}, message={self._message}, \
                created_at={self._created_at})"
    
    def get_response(self):
        return self._responseMovieSearch.json()
    
    def get_movies(self):
        movies =  self.get_response()["results"]
        return movies
    
    def get_titles(self):
        movies = self.get_movies()
        titles = [movie["title"] for movie in movies]
        return titles
    
    def get_ids(self):
        movies = self.get_movies()
        ids = [movie["id"] for movie in movies]
        return ids
    
    def get_best_match_id(self):
        return self.get_ids()[0]
