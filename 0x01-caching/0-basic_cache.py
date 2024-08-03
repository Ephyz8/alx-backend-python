#!/usr/bin/env python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class is a simple caching system without a size limit. """

    def put(self, key, item):
        """ Add an item in the cache.

        Args:
            key: The key associated with the item.
            item: The item to be cached.

        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item by key from the cache.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is None
            or if the key doesn't exist in the cache.
        """
        return self.cache_data.get(key, None)
