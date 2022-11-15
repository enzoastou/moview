"""
Title: main of the Moview project
Authors: Driss BENSAID & Enzo Fragale
Date of creation: 15/11/2022

"""
import requests
import json


text="tenet"
responseMovieSearch = requests.get("https://imdb-api.com/API/SearchMovie/k_djox3zay/" 
                        + text)
movies = responseMovieSearch.json()["results"]
titles = [movie["title"] for movie in movies]
ids = [movie["id"] for movie in movies]

print(titles[0])
print(ids[0])

responseRatings = requests.get("https://imdb-api.com/API/Ratings/k_djox3zay/"
                               + ids[0])
ratings = responseRatings.json()

print(ratings[5:-1])


