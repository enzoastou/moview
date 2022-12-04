# MOVIEW
## Final work in API section of Data Sources class in EPF Montpellier. Started on the 15th of november 2022 by Driss Bensaid and Enzo Fragale.

Moview is a python package that can give you ratings and other useful information about movies by using the imdb API. To use it, one should:
1. Clone this public GitHub repository into their machine by using git
2. Create an account on the imdb API site in order to retrieve a key allowing them to use it
3. Create a ".env" file that needs to be located at your/path/to/moview/.env and with a syntax that should be the following: KEY=xxxxxx
4. Make sure you are at path/to/moview/ and run pip install -r requirements.txt to install dependencies
5. Finally, you can either change the main.py file and adapt it to your needs or import the package and modules you need in another python script

## Documentation
All the 3 modules "movie", "api_calls.movie_search" and "api_calls.ratings_retrieval" have in-code docstrings and comments as well as html documentation that can be found in the html folder from the root.
Feel free to use this documentation when in doubt and, if you cannot manage to find an answer by yourself, please create a github issue with your question or potential bug.

## Technical choices
We decided to respect good practices of code based on the pep8 convention which can be found here: https://pep8.org/ .
We also created an additional score marked on 10 which represents the mean of all the others but this can be disabled with a boolean when instantiating the movie class.*
Different outputs are available including a basic display of ratings as well as User-friendly displays and JSON ones for both the ratings only and also the full description of the selected movie for additional information and/or to ensure it is indeed the movie you wanted ratings on.
Finally, a video presentation from a business standpoint of the "moview" project is available here: https://epfedu-my.sharepoint.com/:v:/g/personal/driss_bensaid_epfedu_fr/EWdaCQg1E0dNun0y35CHXT4BLNE8b1RUBgWEKuGk2-XMNA

I hope we will make your life easier with this module,

Yours truly,

Enzo Fragale