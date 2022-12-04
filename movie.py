"""
Title: main of the Moview project
Authors: Driss BENSAID & Enzo Fragale
Date of creation: 15/11/2022

"""
import json
from api_calls import movie_search
from api_calls import ratings_retrieval

class Movie:
    """
    Contains various functions to retrieve ratings from a movie search request
    on the imdb API.
    """
    _searchTitle=""
    _id=""
    _description=""
    _ratings=""
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, title, includeMoviewScore=True):
        """
        Initalises the class instance based on the title of the movie whose
        ratings need to be retrieved.

        Parameters
        ----------
        title : String
            Represents the title of the movie to be searched.
            
        includeMoviewScore : Boolean, optional
            Whether or not to include the moview score (mean /10 of the others)
            in the ratings list. The default is True.

        Returns
        -------
        None.

        """
        self._searchTitle = title
        movieSearch = movie_search.MovieSearch(title)
        self._description = movieSearch.get_best_match_movie()
        self._id = movieSearch.get_best_match_id()
        ratingsRetrieval = ratings_retrieval.RatingsRetrieval(self._id)
        self._ratings = ratingsRetrieval.get_ratings_list(includeMoviewScore)
        
    def __repr__(self) -> str:
        return f"{type(self).__name__}(type={self._type}, \
                message={self._message}, created_at={self._created_at})"


    def ui_print(self, toPrint=True):
        """
        Returns and/or prints the String of all the ratings line after line
        with format "Reviewer: #, Score: x/10(0)".
        
        Parameters
        ----------
        toPrint : Boolean, optional
            Whether or not to print in the console the ratings.
            The default is True.
        
        Returns
        -------
        StringToPrint : String
            Represents the String containing all the ratings line after line
            with format "Reviewer: #, Score: x/10(0)".

        """
        stringToPrint = ""
        for item in self._ratings:
            # metacritic and rottenTomatoes scores are /100 and not /10
            stringToPrint += \
            ("Reviewer: " + str(item[0]) + ", Score: " + str(item[1]) + "/10")\
                if item[0] not in ["metacritic", "rottenTomatoes"] else\
            ("Reviewer: " + str(item[0]) + ", Score: " + str(item[1]) + "/100")
            stringToPrint += '\n'
        if toPrint:
            print(stringToPrint)
        return stringToPrint
    
    def json_print(self, toPrint=True):
        """
        Returns and/or prints the String of all the ratings as a JSON array
        where JSON objects are of format {"Reviewer": #, "Score": x/10(0)}.
        
        Parameters
        ----------
        toPrint : Boolean, optional
            Whether or not to print in the console the ratings.
            The default is True.
        
        Returns
        -------
        StringToPrint : String
            Represents the JSON String of all the ratings as a JSON array
            where JSON objects are of format {"Reviewer": #, "Score": x/10(0)}.

        """
        stringToPrint = "[{"
        for item in self._ratings:
            # metacritic and rottenTomatoes scores are /100 and not /10
            stringToPrint += \
            ("\"Reviewer\": " + str(item[0]) + ", \"Score\": " + str(item[1])
             + "/10")\
                if item[0] not in ["metacritic", "rottenTomatoes"] else\
            ("\"Reviewer\": " + str(item[0]) + ", \"Score\": " + str(item[1])
             + "/100")
            stringToPrint += '}, {'
        stringToPrint = stringToPrint[:-3] + "]" # removes last comma & bracket
        if toPrint:
            print(stringToPrint)
        return stringToPrint