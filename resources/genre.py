from flask_restful import Resource, reqparse
from flask import request

from scraper import get_genres
from scraper import get_games


class Genre(Resource):
    def get(self, genre):
        params = {
            "genre": genre
        }

        games = get_games(params)

        if games:
            return games, 200
        else:
            return {'message': 'Cannot find games'}, 404


class GenreList(Resource):
    def get(self):
        genres = get_genres()

        if genres:
            return genres, 200
        else:
            return {'message': 'Cannot find genres'}, 404