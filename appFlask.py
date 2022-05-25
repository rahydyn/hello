#!/home/rahydyn/.pyenv/shims/python
# coding: utf-8

import re
from flask import Flask, make_response, abort, jsonify, request
import requests

app = Flask(__name__)

# @app.route('/')
# def index():
#     url = "https://station.ic731.net/api/nearest?lat=36&lon=140&limit=1"
#     payload = {"zn": "1000001"}
#     r = requests.get(url)
#     # r = requests.get(url, prams=payload)
#     return r.json()

@app.route('/', methods=['GET'])
def get_data():
    # try:
        # ここにAPIリクエストを記述
    API_KEY = "94b5670ed2b98460"

    req = request.args
    dic_req = {
        "method": str(request.method),
        "url": str(request.url),
        "lat": str(req.get("lat")),
        "lon": str(req.get("lon")),
        "scheme": str(request.scheme),
        "query_string": str(request.query_string),
        "req": str(req)
    }
    if req.get("lat") is not None:
        lat = req.get("lat")
    else:
        lat = "33.590543"
    if req.get("lon") is not None:
        lon = req.get("lon")
    else:
        lon ="130.420096"

    url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?"
    url += "key="
    url += API_KEY
    url += "&lat="
    url += lat
    url += "&lng="
    url += lon
    url += "&range=2"
    url += "&order=1"
    url += "&format=json"
    url += "&midnight=1"
    url += "&midnight_meal=1"

    # url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=94b5670ed2b98460&lat=33.590543&lng=130.420096&range=2&order=1&format=json&midnight=1&midnight_meal=1"

    try:
        r = requests.get(url)
    except:
        abort(404)    
    # except:
    #     abort(404)

    # 返すjsonを整備
    result = {
        "result": True,
        "data": {
            "latitude": lat,
            "longitude": lon,
        }
    }
    return make_response(jsonify(r.json()))
    # return make_response(jsonify(dic_req))
    # return dic_req

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not Found"}), 404)

if __name__ == '__main__':
    app.run()