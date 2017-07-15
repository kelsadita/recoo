"""
Test class for recoo project
"""
import unittest
import json

from recoo.tastedive import TasteDiveApi


class TasteDiveTest(unittest.TestCase):
    """
    Test class for tastedrive api
    """

    def test_get_recommendations(self):
        """
        Testing get recommendation function from tastedive class
        """
        taste_dive_api = TasteDiveApi()
        parsed_response = taste_dive_api.get_recommendations("inception")
        print(json.dumps(parsed_response))
        self.assertTrue('Similar' in parsed_response)
        self.assertTrue('Info' in parsed_response.get('Similar'))
        self.assertTrue('Results' in parsed_response.get('Similar'))

    def test_get_empty_recommendations(self):
        """
        Testing the empty response for get_recommendations api
        """
        taste_dive_api = TasteDiveApi()
        parsed_response = taste_dive_api.get_recommendations("tochen")
        self.assertTrue('Similar' in parsed_response)
        self.assertTrue('Info' in parsed_response.get('Similar'))
        self.assertTrue('Results' in parsed_response.get('Similar'))

        self.assertEqual(1, len(parsed_response.get('Similar').get('Info')))
        self.assertEqual(0, len(parsed_response.get('Similar').get('Results')))
