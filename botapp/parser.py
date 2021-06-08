import re


class Parser:

    def __init__(self, stop_words):
        self.stop_words = stop_words

    def cleanQuery(self, query):
        """Parse the query input to return the keywords"""
        query_input = re.sub(r"\W+", " ", query).lower()
        query_input = query_input.split(" ")

        parsed_query = []
        for word in self.stop_words:
            if word in query_input:
                query_input.remove(word)
            parsed_query = ' '.join(query_input)
        parsed_query = parsed_query.strip()
        return parsed_query
