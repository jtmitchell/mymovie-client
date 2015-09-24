#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mymovie_unit
----------------------------------

Unit Tests for `mymovie.client` module.
"""

import unittest

from mymovie.search import OMDB
import mock
from tests.mock_utils import MockResponse


class TestMymovieSearch(unittest.TestCase):

    movie_name = 'Casablanca'
    movie_id = '1234567890'

    def setUp(self):
        self.client = OMDB()

    @mock.patch('requests.get')
    def test_search(self, mock_get):
        response_data = dict(Search=[dict(
            Title=self.movie_name,
            imdbID=self.movie_id,
        )])
        mock_response = MockResponse(json_data=response_data, status_code=200)
        mock_get.return_value = mock_response
        results = self.client.search(self.movie_name)
        self.assertListEqual(results, response_data.get('Search'), 'unexpected results')

    @mock.patch('mymovie.search.OMDB.search')
    def test_search_call(self, mock_search):
        self.client.search(self.movie_name)
        mock_search.assert_called_with(self.movie_name)

    @mock.patch('requests.get')
    def test_get(self, mock_get):
        response_data = dict(
            Title=self.movie_name,
            imdbID=self.movie_id,
        )
        mock_response = MockResponse(json_data=response_data, status_code=200)
        mock_get.return_value = mock_response
        results = self.client.get(movie_name=self.movie_name)
        self.assertDictEqual(results, response_data, 'unexpected results')

    @mock.patch('mymovie.search.OMDB.get')
    def test_get_name_call(self, mock_search):
        self.client.get(movie_name=self.movie_name)
        mock_search.assert_called_with(movie_name=self.movie_name)

    @mock.patch('mymovie.search.OMDB.get')
    def test_get_id_call(self, mock_search):
        self.client.get(movie_id=self.movie_id)
        mock_search.assert_called_with(movie_id=self.movie_id)
