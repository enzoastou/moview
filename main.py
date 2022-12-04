"""
Title: main of the Moview project
Authors: Driss BENSAID & Enzo Fragale
Date of creation: 15/11/2022

"""

# Example of how to use the package:

# Import module
import movie

# Set movie title to look ratings for
title = "inception"

# Instantiate Movie class from title
movie = movie.Movie(title)

# Choose the best way for you to print the results

print(movie.get_ratings_list())
movie.ui_print()
movie.json_full_print()
