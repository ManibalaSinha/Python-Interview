from collections import OrderedDict #OrderedDict, which maintains insertion order (critical for LRU logic)

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict() #self.cache: stores key-value pairs with order
        self.capacity = capacity #self.capacity: max items allowed

    def get(self, key: int) -> int:
        if key not in self.cache: #check whether key exists
            return -1 #otherwise
        # Move to end to mark as recently used
        self.cache.move_to_end(key) #If key exists, move it to the end to mark as recently used, & return the value
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update and mark as recently used
            self.cache.move_to_end(key) #move it to end
        self.cache[key] = value #Insert the key-value
        if len(self.cache) > self.capacity: #If over capacity
            # Pop the least recently used (first) item
            self.cache.popitem(last=False)
#ex
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # returns 1