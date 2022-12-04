"""
Title: ratings_retrieval module of the Moview project
Authors: Driss BENSAID & Enzo Fragale
Date of creation: 15/11/2022

"""
import requests
import os
from dotenv import load_dotenv

class RatingsRetrieval:
    """
    Contains various functions to retrieve ratings from a movie id on the imdb
    API.
    """
    _movieId=""
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
        self._movieId = id
        load_dotenv()
        apiKey=os.getenv("KEY")
        self._responseRatings = requests.get(
            "https://imdb-api.com/API/Ratings/" + apiKey + "/" 
            + self._movieId)
        
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
    
    def get_ratings_list(self, includeMoviewScore=True):
        """
        Gets and returns all the ratings on the id passed when intialising the 
        class instance as a list of strings.
        
        Parameters
        ----------
        includeMoviewScore : Boolean, optional
            Whether or not to include the moview score (mean /10 of the others)
            in the ratings list. The default is True.

        Returns
        -------
        ratingsList : String list
            All the ratings on the id passed when intialising the class
            instance as a list of strings.

        """
        ratings =  self.get_response()
        ratingsList = list(ratings.items())[5:-1]
        
        #moview score is just the out of 10 mean rating of all other ones
        if includeMoviewScore:
            sum=0
            for item in ratingsList:
                # metacritic and rottenTomatoes scores are /100 and not /10
                sum += float(item[1]) if item[0] not in ["metacritic", \
                       "rottenTomatoes"] else float(item[1])/10
            ratingsList.append(("moview", sum/5))
        return ratingsList
