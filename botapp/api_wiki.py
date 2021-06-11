import wikipedia


class WikiApi:

    def __init__(self):
        wikipedia.set_lang("fr")

    def get_wiki_result(self, lat, lng, query_parse):
        """Return the summary and the url of the wikipedia page searched with the query parsed. If nothing
        fund with the query, search with the latitude and longitude in addition to the query """
        try:
            page = wikipedia.page(query_parse)
            return {
                "summary": page.summary[:600],
                "url": page.url
            }

        except (wikipedia.exceptions.PageError):
            return False

        except (wikipedia.exceptions.DisambiguationError):
            try:
                geosearch_result = wikipedia.geosearch(lat, lng, query_parse)
                page = wikipedia.page(geosearch_result[0])
                return {
                    "summary": page.summary[:500],
                    "url": page.url
                }

            except IndexError:

                return False

            except (wikipedia.exceptions.DisambiguationError):

                return False
