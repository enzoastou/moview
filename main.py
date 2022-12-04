"""
Title: main of the Moview project
Authors: Driss BENSAID & Enzo Fragale
Date of creation: 15/11/2022

"""
import json

from api_calls import movie_search
from api_calls import ratings_retrieval

text="inception"

movieSearch = movie_search.MovieSearch(text)
bestMatchId = movieSearch.get_best_match_id()
ratingsRetrieval = ratings_retrieval.RatingsRetrieval(bestMatchId)
ratingsList = ratingsRetrieval.get_ratings_list()
print(ratingsList)

def ui_print(ratingsList, includeMoviewScore=False):
    #if includeMoviewScore:
        #if ratingsList[] not in ["metacritic", "rottenTomatoes"]
        #mean = ratingsList[:,1].sum()
        #ratingsList.append(mean)
    for item in ratingsList:
        print("Reviewer: " + str(item[0]) + ", Score: " + str(item[1]) + "/10")\
        if item[0] not in ["metacritic", "rottenTomatoes"] else\
        print("Reviewer: " + str(item[0]) + ", Score: " + str(item[1]) + "/100")
        
ui_print(ratingsList)




#import argparse

#parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
#parser.add_argument('--workspace', metavar='path', required=True, help='the path to workspace')
#args = parser.parse_args()
#main(workspace=args.workspace, schema=args.schema, dem=args.dem)