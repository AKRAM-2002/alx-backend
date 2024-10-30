#!/usr/bin/python3
""" Basic Dictionary module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''
    Basic caching implementation.
    '''

    def put(self, key, item):
        '''
        Add an item to the cache with a given key.
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        '''
        Retrieve the item associated with a given key
        from the cache.
        '''
        return self.cache_data.get(key, None)
