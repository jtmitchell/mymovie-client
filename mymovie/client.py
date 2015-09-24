# -*- coding: utf-8 -*-
import requests

DEFAULT_URL = 'http://mymovie-api.maungawhau.net.nz/api/v1'


class Watchlist(object):
    """Client object for communicating with the server."""

    def __init__(self, user, password, url=None):
        self.url = DEFAULT_URL if url is None else url
        self.token = self.auth(user, password)
        self.headers = dict(
            content_type='application/json',
            authorization='JWT {0}'.format(self.token),
        )

    def auth(self, user, password):
        """Authenticate with the server, and return the API token for other calls."""
        data = dict(
            username=user,
            password=password,
        )
        response = requests.post(
            url=self.url + '/auth/login',
            data=data,
        )

        if response.ok:
            result = response.json()
            return result.get('token')

    def user_details(self):
        """Get the user details after login."""
        response = requests.get(
            url=self.url + '/users/me',
            headers=self.headers,
        )
        if response.ok:
            return response.json()

    def list(self):
        """List the watchlist items for this user."""
        response = requests.get(
            url=self.url + '/watchlists',
            headers=self.headers,
        )
        if response.ok:
            return response.json()

    def get(self, list_id):
        """Get a specific watchlist item.
        {
            "id": 1,
            "movie":
                {
                    "id": 1,
                    "name": "Star Trek",
                    "poster": "<image url>"
                    "year": 2009,
                    "services":
                        [
                            {...}
                        ]
                },
            "notifications":
                [
                    {
                        "id": 1,
                        "type": 0,
                        "watchlist": 1,
                        "notified": false,
                        "notified_date": ""
                    }
                ]
        }
        """
        response = requests.get(
            url=self.url + '/watchlists/{0}'.format(list_id),
            headers=self.headers,
        )
        if response.ok:
            return response.json()

    def delete(self, list_id):
        """Delete a single watchlist item"""
        response = requests.delete(
            url=self.url + '/watchlists/{0}'.format(list_id),
            headers=self.headers,
        )
        if response.ok:
            return True
        else:
            return False

    def create(self, data):
        """Create a new watchlist item.
        {
            "moviename": "Star Trek",
            "service": "omdb",
            "service_id": "tt0796366"
            "notifywhen":
                [
                    0, 2, 3
                ]
        }
        """
        response = requests.post(
            url=self.url + '/watchlists',
            params=data,
            headers=self.headers,
        )
        if response.ok:
            return response.json()

    def update(self, list_id, data):
        """Update the details for a watchlist item."""
        response = requests.put(
            url=self.url + '/watchlists/{0}'.format(list_id),
            params=data,
            headers=self.headers,
        )
        if response.ok:
            return response.json()
