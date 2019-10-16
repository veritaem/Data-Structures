from doubly_linked_list import *


class LRUCache:
    def __init__(self, limit=10):
        self.cache = []
        self.limit = limit
    
    def index_of(self, key):
        matches = [i for i, (k, v) in enumerate(self.cache) if k == key] 
        if len(matches):
            print(matches[0], 'match')
        return matches[0] if len(matches) else None # finds cache key that has value, returns first
    
    def get(self, key):
        i = self.index_of(key)
        if i:
            self.cache = [self.cache.pop(i)] + self.cache
            return self.cache[0][1]
        else:
            return None


    def set(self, key, value):
        i = self.index_of(key)

        if i:
            self.cache[i] = (key, value)
        else:
            self.cache = [(key, value)] + self.cache

            if self.limit < len(self.cache):
                self.cache.pop(-1)
    
