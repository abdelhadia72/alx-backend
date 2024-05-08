#!/usr/bin/env python3
""" File mru cache """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ mru cache class """

    def __init__(self):
        super().__init__()
        self.use_order = []

    def put(self, key, item):
        """ put method """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.use_order.pop()
                print("DISCARD: {}".format(mru_key))
                del self.cache_data[mru_key]
            self.cache_data[key] = item
            if key in self.use_order:
                self.use_order.remove(key)
            self.use_order.append(key)

    def get(self, key):
        """ get method """
        if key is None or key not in self.cache_data:
            return None

        if key in self.use_order:
            self.use_order.remove(key)
        self.use_order.append(key)

        return self.cache_data[key]
