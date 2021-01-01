"""
LRU Cache

This problem was recently asked by Apple:

LRU cache is a cache data structure that has limited space,
and once there are more items in the cache than available space,
it will preempt the least recently used item.

What counts as recently used is any item a key has 'get' or 'put' called on it.

Implement an LRU cache class with the 2 functions 'put' and 'get'.
'put' should place a value mapped to a certain key, and preempt items if needed.
'get' should return the value for a given key if it exists in the cache,
and return None if it doesn't exist.

"""
from collections import OrderedDict


class LRUCache:
    def __init__(self, space):
        self.space = space
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None

        value = self.cache[key]
        del self.cache[key]

        self.cache[key] = value
        return value

    def put(self, key, value):
        if key not in self.cache:
            self.cache[key] = value

            if len(self.cache) > self.space:
                self.cache.popitem(last=False)

        else:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(3, 3)
    cache.put(4, 4)

    print(cache.get(3))
    # 3
    print(cache.get(2))
    # None

    cache.put(2, 2)

    print(cache.get(4))
    # None (pre-empted by 2)
    print(cache.get(3))
    # 3
