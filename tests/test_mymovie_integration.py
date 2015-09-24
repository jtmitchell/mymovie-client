#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mymovie
----------------------------------

Tests for `mymovie.client` module.
"""

import unittest

from mymovie import client, search
from mymovie.search import OMDB


class TestMymovieClient(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        pass

    def tearDown(self):
        pass


class TestMymovieSearch(unittest.TestCase):

    movie_name = 'Casablanca'
    movie_id = 'tt0034583'

    def setUp(self):
        self.client = OMDB()

    def test_search_success(self):
        results = self.client.search(self.movie_name)
        self.assertIsInstance(results, list, '{0} is not a list'.format(results))
        self.assertGreater(
            len(results), 0, 'did not get results for "{0}" search'.format(self.movie_name))
        self.assertIn('Title', results[0], 'result has no title')
        self.assertIn('imdbID', results[0], 'result has no imdb ID')

    def test_get_name(self):
        results = self.client.get(movie_name=self.movie_name)
        self.assertIn('Title', results, 'result has no title')
        self.assertEqual(self.movie_name, results.get(
            'Title'), '"{0}" title does not match "{1}"'.format(results.get('Title'), self.movie_name))
        self.assertIn('imdbID', results, 'result has no imdb ID')
        self.assertEqual(self.movie_id, results.get(
            'imdbID'), '"{0}" title does not match "{1}"'.format(results.get('imdbID'), self.movie_id))

    def test_get_id(self):
        results = self.client.get(movie_id=self.movie_id)
        self.assertIn('Title', results, 'result has no title')
        self.assertEqual(self.movie_name, results.get(
            'Title'), '"{0}" title does not match "{1}"'.format(results.get('Title'), self.movie_name))
        self.assertIn('imdbID', results, 'result has no imdb ID')
        self.assertEqual(self.movie_id, results.get(
            'imdbID'), '"{0}" title does not match "{1}"'.format(results.get('imdbID'), self.movie_id))
