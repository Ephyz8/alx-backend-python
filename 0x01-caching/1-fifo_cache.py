#!/usr/bin/env python3
""" FIFOCache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class is a caching system: First-In, First-Out algorithm. """

    def __init__(self):
        """ Initialize the cache and order tracking list. """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Add an item in the cache.

        Args:
            key: The key associated with the item.
            item: The item to be cached.

        If key or item is None, this method does nothing.
        If the number of items in self.cache_data exceeds MAX_ITEMS, the first
        item put in cache is discarded following FIFO algorithm.
        """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            self.keys_order.append(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.keys_order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """ Retrieve an item by key from the cache.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is None
            or if the key doesn't exist in the cache.
        """
        return self.cache_data.get(key)
