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
    _searchedTitle=""
    _movieId=""
    _movieDescription=""
    _ratingsList=""
    
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
        self._searchedTitle = title
        movieSearch = movie_search.MovieSearch(self._searchedTitle)
        self._movieDescription = movieSearch.get_best_match_description()
        self._movieId = movieSearch.get_best_match_id()
        ratingsRetrieval = ratings_retrieval.RatingsRetrieval(self._movieId)
        self._ratingsList = ratingsRetrieval.get_ratings_list(includeMoviewScore)
        
    def __repr__(self) -> str:
        return f"{type(self).__name__}(type={self._type}, \
                message={self._message}, created_at={self._created_at})"
    
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
        ratingsList =  self._ratingsList
        return ratingsList


    def ui_print(self, toPrint=True):
        """
        Returns and/or prints the String of all the ratings line after line
        with format "reviewer: #, score: x/10(0) ;".
        
        Parameters
        ----------
        toPrint : Boolean, optional
            Whether or not to print in the console the ratings.
            The default is True.
        
        Returns
        -------
        StringToPrint : String
            Represents the String containing all the ratings line after line
            with format "reviewer: #, score: x/10(0) ;".

        """
        stringToPrint = ""
        for item in self._ratingsList:
            # metacritic and rottenTomatoes scores are /100 and not /10
            stringToPrint += \
            ("reviewer: " + str(item[0]) + ", score: " + str(item[1]) + "/10")\
                if item[0] not in ["metacritic", "rottenTomatoes"] else\
            ("reviewer: " + str(item[0]) + ", score: " + str(item[1]) + "/100")
            stringToPrint += ' ;\n'
        stringToPrint = stringToPrint[:-4] # removes last semi-colon & \n
        if toPrint:
            print(stringToPrint)
        return stringToPrint
    
    def json_print(self, toPrint=True):
        """
        Returns and/or prints the String of all the ratings as a JSON array
        where JSON objects are of format {"reviewer": #, "score": x/10(0)}.
        
        Parameters
        ----------
        toPrint : Boolean, optional
            Whether or not to print in the console the ratings.
            The default is True.
        
        Returns
        -------
        StringToPrint : String
            Represents the JSON String of all the ratings as a JSON array
            where JSON objects are of format {"reviewer": #, "score": x/10(0)}.

        """
        stringToPrint = "[{"
        for item in self._ratingsList:
            # metacritic and rottenTomatoes scores are /100 and not /10
            stringToPrint += \
            (""""reviewer": """ + str(item[0]) + ", """"score": """"" + str(item[1])
             + "/10")\
                if item[0] not in ["metacritic", "rottenTomatoes"] else\
            (""""reviewer": """ + str(item[0]) + ", """"score": """"" + str(item[1])
             + "/100")
            stringToPrint += '}, {'
        stringToPrint = stringToPrint[:-3] + "]" # removes last comma & bracket
        if toPrint:
            print(stringToPrint)
        return stringToPrint
    
    def ui_full_print(self, toPrint=True):
        """
        Returns and/or prints the String fully describing the selected movie as
        well as all the ratings line after line with format
        "field: value ;"
        "reviewer: #, score: x/10(0) ;".

        Parameters
        ----------
        toPrint : Boolean, optional
            Whether or not to print in the console the ratings.
            The default is True.

        Returns
        -------
        StringToPrint : String
           Represents the String fully describing the selected movie as well as
           all the ratings line after line with format
           "field: value ;"
           "reviewer: #, score: x/10(0) ;".

        """
        
        stringToPrint = ""
        for key, value in self._movieDescription.items():
            stringToPrint += key + ': ' + value + " ;\n"
        stringToPrint += self.ui_print(toPrint=False)
        if toPrint:
            print(stringToPrint)
        return stringToPrint
    
    def json_full_print(self, toPrint=True):
        """
        Returns and/or prints the String fully describing the selected movie as
        well as all the ratings as a JSON object where lines are of format
        {"field": #,
         "ratings": [{"reviewer": #, "score": x/10(0)},
                      {"reviewer": #, "score": x/10(0)}]
        }.

        Parameters
        ----------
        toPrint : Boolean, optional
            Whether or not to print in the console the ratings.
            The default is True.

        Returns
        -------
        StringToPrint : String
           Represents the String fully describing the selected movie as
           well as all the ratings as a JSON object where lines are of format
           {"field": #,
            "ratings": [{"reviewer": #, "score": x/10(0)},
                         {"reviewer": #, "score": x/10(0)}]
           }.

        """
        movieDictionary = self._movieDescription
        movieDictionary["ratings"] = ""
        stringToPrint = json.dumps(movieDictionary)
        stringToPrint = stringToPrint[:-3] + (self.json_print(False)) + '}'
        if toPrint:
            print(stringToPrint)
        return stringToPrint