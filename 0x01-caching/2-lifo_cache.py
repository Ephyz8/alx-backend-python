#!/usr/bin/env python3
"""Task 2: LIFO Caching.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LIFO
    removal mechanism when the limit is reached.
    """
    def __init__(self):
        """Initializes the cache
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by key
        """
        return self.cache_data.get(key, None)
    
#!/usr/bin/env python3
""" LIFOCache module """

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class is a caching system: (Last-In, First-Out) algorithm."""

    def __init__(self):
        """Initialize the cache and order tracking list."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key: The key associated with the item.
            item: The item to be cached.

        If key or item is None, this method does nothing.
        If the number of items in self.cache_data exceeds MAX_ITEMS, the last
        item put in cache is discarded following the LIFO algorithm.
        """
        if key is None or item is None:
            return

        # If the key is not already in cache_data, and adding it will exceed MAX_ITEMS, evict the last item
        if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Pop the last item (most recently added) in LIFO manner
            last_key, _ = self.cache_data.popitem(last=True)
            print("DISCARD:", last_key)

        # Add or update the item in the cache
        self.cache_data[key] = item

        # Move the key to the end to signify it as the most recently used
        self.cache_data.move_to_end(key)

    def get(self, key):
        """Retrieve an item by key from the cache.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The item associated with the key, or None if the key is None
            or if the key doesn't exist in the cache.
        """
        return self.cache_data.get(key)
