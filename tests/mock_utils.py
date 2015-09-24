# -*- coding: utf-8 -*-


class MockResponse(object):

    def __init__(self, json_data=None, status_code=None, *args, **kwargs):
        self.json_data = json_data if json_data else {}
        self.status_code = status_code if status_code else 404

    @property
    def ok(self):
        if self.status_code >= 200 and self.status_code < 400:
            return True
        return False

    def json(self):
        return self.json_data
