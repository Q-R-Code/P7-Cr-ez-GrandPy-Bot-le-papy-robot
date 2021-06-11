"""
Simple test unitaire with pytest.
"""

from botapp.parser import Parser
from botapp.constantes import STOP_WORDS


class TestParser:
    QUERY = "Bonjour, ou ce trouve la FNAC à Amiens ?"
    PARSE_QUERY_EXPECTED = "fnac amiens"

    def test_parse_query(self):
        query_send = self.QUERY
        parser = Parser(stop_words=STOP_WORDS)
        query_parse = parser.cleanQuery(query_send)

        assert query_parse == self.PARSE_QUERY_EXPECTED
