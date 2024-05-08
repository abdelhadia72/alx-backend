""" File lfu cache """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ lfu cache class """

    def __init__(self):
        super().__init__()
        self.use_order = {}

    def put(self, key, item):
        """ put method """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key =

    def get(self, key):
        """ get method """
        if key is None or key not in self.cache_data:
            return None

        if key in self.use_order:
            self.use_order.remove(key)
        self.use_order.append(key)

        return self.cache_data[key]
