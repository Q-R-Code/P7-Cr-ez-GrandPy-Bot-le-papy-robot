import random

from flask import Flask, render_template, jsonify, request
from config import GMAPS_KEY
from botapp.api_wiki import WikiApi
from botapp.constantes import STOP_WORDS, MSG_GMAPS_OK, MSG_WIKI_OK, MSG_FAIL
from botapp.api_gmaps import GmapsApi
from botapp.parser import Parser
from run import app


# Init the Parser class
parser = Parser(STOP_WORDS)
# Init the class for GmapsApi
gmaps_api = GmapsApi()
# Init the WikiApi class
wiki_api = WikiApi()


@app.route('/')
def index():
    return render_template('index.html', gmaps_key=GMAPS_KEY)


@app.route('/query')
def query_json():
    query_input = request.args.get('query', type=str)
    query_parse = parser.cleanQuery(query_input)
    if query_parse != "":
        gmap_search = gmaps_api.get_position(query_parse)
        gmap_lat = gmap_search["latitude"]
        gmap_lng = gmap_search["longitude"]
        gmap_address = gmap_search["address"]
        if gmap_search:
            msg_gmaps_ok = "{} {}".format(random.choice(MSG_GMAPS_OK), gmap_address)
            wiki_results = wiki_api.get_wiki_result(gmap_lat, gmap_lng, query_parse)
            if wiki_results:
                msg_wiki_ok = "{} {}...({})".format(random.choice(MSG_WIKI_OK), wiki_results["summary"],
                                                    wiki_results["url"])
                return jsonify(lat=gmap_lat,
                               lng=gmap_lng,
                               msg_gmaps=msg_gmaps_ok,
                               msg_wiki=msg_wiki_ok,
                               msg_fail=None,
                               error=False)
            else:
                app.logger.info('Failed to find Wiki result')
                msg_fail = "{}".format(random.choice(MSG_FAIL))
                return jsonify(msg_fail=msg_fail, error=True)
        else:
            app.logger.info('Failed to find Gmaps result')
            msg_fail = "{}".format(random.choice(MSG_FAIL))
            return jsonify(msg_fail=msg_fail, error=True)


if __name__ == "__main__":
    app.run()
