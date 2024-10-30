#!/usr/bin/python3
""" LRU caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict
from functools import lru_cache


class LRUCache(BaseCaching):
    '''
    LIFO (Last In, First Out) Cache Implementation
    Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached
    '''

    def __init__(self):
        super().__init__()
        self.usedKey = []

    def put(self, key, item):
        '''
        Add an item to the cache with a given key.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.usedKeys:
                self.usedKeys.append(key)
            else:
                self.usedKeys.append(
                    self.usedKeys.pop(self.usedKeys.index(key)))
            if len(self.usedKeys) > BaseCaching.MAX_ITEMS:
                discard = self.usedKeys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        '''
        Retrieve an item from the cache with a given key.
        '''
        if key is not None and key in self.cache_data.keys():
            self.usedKeys.append(self.usedKeys.pop(self.usedKeys.index(key)))
        return self.cache_data.get(key, None)
