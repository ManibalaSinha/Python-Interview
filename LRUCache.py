#Implement LRU(Least Recently Used) cache in python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the key to the end to show it's recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update the value and mark as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Pop the first (least recently used) item
            self.cache.popitem(last=False)
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))