"""
Title: main of the Moview project
Authors: Driss BENSAID & Enzo Fragale
Date of creation: 15/11/2022

"""
import movie

text="inception"

movie = movie.Movie(text)

movie.json_print()




#import argparse

#parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
#parser.add_argument('--workspace', metavar='path', required=True, help='the path to workspace')
#args = parser.parse_args()
#main(workspace=args.workspace, schema=args.schema, dem=args.dem)