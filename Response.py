import requests
#import requests_cache

from flask import Flask, jsonify, abort, make_response
from flask.ext.restful import Api, Resource, reqparse, fields, marshal

app = Flask(__name__, static_url_path="")
api = Api(app)



@app.route('/dir', methods='GET')
@api.representations
def dir():
    resp = DownloadListing.get_results()
    resp = make_response(json_dumps)

