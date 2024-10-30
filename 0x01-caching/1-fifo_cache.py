#!/usr/bin/python3
""" FIFO caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict

class FIFOCache(BaseCaching):
    '''
    FIFO (First In, First Out) Cache Implementation
    Represents an object that allows storing and
    retrieving items from a dictionary with a FIFO
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
            if len(self.cache_data) > BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
                '''
                If cache is full, remove the least recently used item
                '''
                oldest_key, _ = self.cache_data.popitem(False)
                print("DISCARD: {}".format(oldest_key))
            self.cache_data[key] = item

    def get(self, key):
        '''
        Retrieve an item from the cache with a given key.
        '''
        return self.cache_data.get(key, None)
