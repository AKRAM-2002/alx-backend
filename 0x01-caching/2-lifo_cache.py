#!/usr/bin/python3
""" LIFO caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict

class LIFOCache(BaseCaching):
    '''
    LIFO (Last In, First Out) Cache Implementation
    Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached
    '''
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
    
    def put(self, key, item):
        '''
        Add an item to the cache with a given key.
        '''
        if key is None or item is None:
            return
        else:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''
        Retrieve an item from the cache with a given key.
        '''
        return self.cache_data.get(key, None)
