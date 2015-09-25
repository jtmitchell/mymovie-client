# -*- coding: utf-8 -*-

"""
test_mymovie_unit
----------------------------------

Unit Tests for `mymovie.client` module.
"""

import unittest

import mock
from mock.mock import ANY

from mymovie.__main__ import main
from mymovie.client import Watchlist
from mymovie.search import OMDB
from tests.mock_utils import MockResponse


class TestMymovieWatchlist(unittest.TestCase):

    def setUp(self):
        self.client = Watchlist()
        self.url = self.client.url
        self.client.token = '123.456.789'
        self.client._set_header()

    @mock.patch('requests.post')
    def test_auth(self, mock_post):
        user = 'Test'
        password = 'test001'
        self.client.auth(user, password)
        mock_post.assert_called_with(
            data=dict(
                username=user,
                password=password,
            ),
            url=self.url + '/auth/login',
        )

    @mock.patch('requests.get')
    def test_user_details(self, mock_get):
        self.client.user_details()
        mock_get.assert_called_with(
            url=self.url + '/users/me',
            headers=self.client.headers,
        )

    @mock.patch('requests.get')
    def test_list(self, mock_get):
        self.client.list()
        mock_get.assert_called_with(
            url=self.url + '/watchlists',
            headers=self.client.headers,
        )

    @mock.patch('requests.get')
    def test_get(self, mock_get):
        list_id = "1"
        self.client.get(list_id)
        mock_get.assert_called_with(
            url=self.url + '/watchlists/' + list_id,
            headers=self.client.headers,
        )

    @mock.patch('requests.delete')
    def test_delete(self, mock_delete):
        list_id = "1"
        self.client.delete(list_id)
        mock_delete.assert_called_with(
            url=self.url + '/watchlists/' + list_id,
            headers=self.client.headers,
        )

    @mock.patch('requests.post')
    def test_create(self, mock_post):
        movie_data = dict(
            moviename="Star Trek",
            service="omdb",
            service_id="tt0796366",
            notifywhen=[0, 2, 3],
        )

        self.client.create(movie_data)
        mock_post.assert_called_with(
            url=self.url + '/watchlists',
            headers=self.client.headers,
            params=movie_data,
        )

    @mock.patch('requests.put')
    def test_update(self, mock_put):
        list_id = "1"
        movie_data = dict()
        self.client.update(list_id, movie_data)
        mock_put.assert_called_with(
            url=self.url + '/watchlists/' + list_id,
            headers=self.client.headers,
            params=movie_data,
        )


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

    @mock.patch('mymovie.search.OMDB.search')
    def test_search_cmdline(self, mock_search):
        main(['-s', self.movie_name])
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

    @mock.patch('mymovie.search.OMDB.get')
    def test_get_id_cmdline(self, mock_search):
        main(['-i', self.movie_id])
        mock_search.assert_called_with(movie_id=self.movie_id)
