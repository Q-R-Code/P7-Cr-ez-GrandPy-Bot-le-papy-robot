""":return secret key and googlemaps key from os.environ"""

import os

SECRET_KEY = os.environ.get('SECRET_KEY')

GMAPS_KEY = os.environ.get('GMAPS_KEY')
