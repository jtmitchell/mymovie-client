# -*- coding: utf-8 -*-
from urllib.parse import quote_plus

import requests


class OMDB(object):
    """Search against the Open Movie DB"""

    base_url = 'http://www.omdbapi.com/'

    def __init__(self, url=None):
        if url:
            self.base_url = url

    def search(self, search_term, search_type='movie'):
        params = dict(
            t=search_type,
            s=quote_plus(search_term),
        )
        response = requests.get(
            url=self.base_url,
            params=params,
        )
        if response.ok:
            return response.json().get('Search', [])

    def get(self, movie_id=None, movie_name=None):
        params = dict(tomatoes=True)
        if movie_id:
            params.update(dict(i=movie_id))
        if movie_name:
            params.update(dict(t=movie_name))
        response = requests.get(
            url=self.base_url,
            params=params,
        )
        if response.ok:
            return response.json()
