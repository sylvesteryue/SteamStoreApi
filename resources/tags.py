from flask_restful import Resource, reqparse
from flask import request

from scraper import get_tags
from scraper import get_games

class Tag(Resource):
    def get(self, tag_id):
        params = {
            "tags": tag_id
        }

        games = get_games(params)

        if games:
            return games, 200
        else:
            return {'message': 'Cannot find games'}, 404



class TagsList(Resource):
    def get(self):
        tags = get_tags()

        if tags:
            return tags, 200
        else:
            return {'message': 'Cannot find tags'}, 404