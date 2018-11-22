#!/usr/bin/python
# coding=utf-8
import json
from pithy import request
from pithy import config_manager

config = config_manager()


class PithyAPP(object):

    def __init__(self):
        self.base_url = config['BASE_URL']

    @request(url='/get')
    def get(self, key1='value1', key2=None):
        """
        get method
        """
        if key2 is None:
            key2 = ['value2', 'value3']

        params = {
            'key1': key1,
            'key2': key2
        }
        return dict(params=params)

    @request(url='post', method='post')
    def post(self, key1='value1'):
        """
        post method
        """
        data = {
            'key1': key1
        }
        return dict(data=data)

    @request(url='post', method='post')
    def json(self, key1='value1'):
        """
        post method
        """
        json = {
            'key1': key1
        }
        return dict(json=json)

