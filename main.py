from flask import Flask, jsonify
from flask_restful import Api

from resources.tags import Tag, TagsList
from resources.genre import Genre, GenreList

app = Flask(__name__)
api = Api(app)

api.add_resource(TagsList, '/tags')
api.add_resource(Tag, '/tags/<string:tag_id>')
api.add_resource(GenreList, '/genre')
api.add_resource(Genre, '/genre/<string:genre>')



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)