from flask_restful import Resource, reqparse
from flask import request

from scraper import get_games

class Specials(Resource):
    def get(self):

        params = {
            "specials": '1'
        }

        games = get_games(params)

        if games:
            return games, 200
        else:
            return {'message': 'Cannot find games'}, 404