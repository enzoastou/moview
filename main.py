"""
Title: main of the Moview project
Authors: Driss BENSAID & Enzo Fragale
Date of creation: 15/11/2022

"""
import requests
import json

from api_calls import movie_search
from api_calls import ratings_retrieval


text="inception"
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

ratingsList=list(ratings.items())[5:-1]

def UIprint(ratingsList, includeMoviewScore=False):
    #if includeMoviewScore:
        #if ratingsList[] not in ["metacritic", "rottenTomatoes"]
        #mean = ratingsList[:,1].sum()
        #ratingsList.append(mean)
    for item in ratingsList:
        print("Reviewer: " + str(item[0]) + ", Score: " + str(item[1]) + "/10")\
        if item[0] not in ["metacritic", "rottenTomatoes"] else\
        print("Reviewer: " + str(item[0]) + ", Score: " + str(item[1]) + "/100")
        
UIprint(ratingsList)


#import argparse

#parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
#parser.add_argument('--workspace', metavar='path', required=True, help='the path to workspace')
#args = parser.parse_args()
#main(workspace=args.workspace, schema=args.schema, dem=args.dem)