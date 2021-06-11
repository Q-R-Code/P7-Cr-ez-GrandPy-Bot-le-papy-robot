"""
Simple unitaire Test with pytest.
For each one, use mock to copy the behavior of API modules googlemaps and wikipedia.

"""

from botapp.api_gmaps import GmapsApi
from botapp.api_wiki import WikiApi


class TestGmaps:
    QUERY_PARSE = "fnac amiens"

    def test_gmaps_result(self, monkeypatch):
        result = {
            "address": "12 Rue des 3 Cailloux, 80000 Amiens, France",
            "latitude": "49.8925929",
            "longitude": "2.2984867",
        }

        def mockreturn(self, query):
            return result

        monkeypatch.setattr(GmapsApi, 'get_position', mockreturn)
        gmap_results = GmapsApi().get_position(self.QUERY_PARSE)

        assert gmap_results["address"] == "12 Rue des 3 Cailloux, 80000 Amiens, France"
        assert gmap_results["latitude"] == "49.8925929"
        assert gmap_results["longitude"] == "2.2984867"


class TestWiki:
    LATITUDE = "49.8925929"
    LONGITUDE = "2.2984867"
    QUERY_PARSE = "fnac amiens"

    def test_wiki_api(self, monkeypatch):
        result = {
            "summary": "Regarde-moi est le sixième album studio de la chanteuse française Lorie, sorti le 21 novembre "
                       "2011 chez Columbia Records. Le premier extrait est le titre Dita.\nAvec 2lor en moi ? sorti"
                       " en 2007, il s'agit du second album de Lorie depuis son changement de production et de maison"
                       " de disque.\nCet album, aux sons très électro, est selon Lorie, le plus personnel et le plus "
                       "intime de sa carrière.",
            "url": "https://fr.wikipedia.org/wiki/Regarde-moi"
        }

        def mockreturn(self, lat, lng, query_parse):
            return result

        monkeypatch.setattr(WikiApi, 'get_wiki_result', mockreturn)
        wiki_results = WikiApi().get_wiki_result(self.LATITUDE, self.LONGITUDE, self.QUERY_PARSE)

        assert wiki_results["summary"] == "Regarde-moi est le sixième album studio de la chanteuse française Lorie," \
                                          " sorti le 21 novembre 2011 chez Columbia Records. Le premier extrait est le" \
                                          " titre Dita.\nAvec 2lor en moi ? sorti en 2007, il s'agit du second album de" \
                                          " Lorie depuis son changement de production et de maison de disque.\nCet" \
                                          " album, aux sons très électro, est selon Lorie, le plus personnel et le" \
                                          " plus intime de sa carrière."
        assert wiki_results["url"] == "https://fr.wikipedia.org/wiki/Regarde-moi"
