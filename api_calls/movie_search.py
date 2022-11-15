"""
Title: movie_search module of the Moview project
Authors: Driss BENSAID & Enzo Fragale
Date of creation: 15/11/2022

"""
import requests
import json

class MovieSearch:
    _searchTitle=""
    _responseMovieSearch=""
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, title):
        self._searchTitle = title
        self._responseMovieSearch = requests.get("https://imdb-api.com/API/SearchMovie/k_djox3zay/" 
                                + self._searchTitle)
    def __repr__(self) -> str:
        return f"{type(self).__name__}(type={self._type}, message={self._message}, created_at={self._created_at})"
    
    movies = responseMovieSearch.json()["results"]
    titles = [movie["title"] for movie in movies]
    ids = [movie["id"] for movie in movies]

    print(titles[0])
    print(ids[0])
