"""
Title: ratings_retrieval module of the Moview project
Authors: Driss BENSAID & Enzo Fragale
Date of creation: 15/11/2022

"""
import requests
import json

class Rating:
    _created_at=""
    
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    def __init__(self, Type, message, created_at):
        self._type = Type
        self._message = message
        self._created_at = created_at
    def __repr__(self) -> str:
        return f"{type(self).__name__}(type={self._type}, message={self._message}, created_at={self._created_at})"