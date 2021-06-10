import googlemaps

from googlemaps.geocoding import geocode
from config import GMAPS_KEY


class GmapsApi:

    def __init__(self):
        self.client = googlemaps.Client(GMAPS_KEY)

    def get_position(self, query):
        """Return the position of the query parsed"""
        geocoding = geocode(self.client, query)

        try:
            address = geocoding[0]["formatted_address"]
            lat = geocoding[0]["geometry"]["location"]["lat"]
            lng = geocoding[0]["geometry"]["location"]["lng"]

            return {
                "address": address,
                "latitude": lat,
                "longitude": lng,
            }
        except IndexError:
            return False
