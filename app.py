from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from flask_pymongo import pymongo

from myapp.endpoints import api_routes


def create_app():
    web_app = Flask(__name__)  
    CORS(web_app)
    api_blueprint = Blueprint('api_blueprint', __name__)
    api_blueprint = api_routes(api_blueprint)
    web_app.register_blueprint(api_blueprint)
    return web_app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
