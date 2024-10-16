lru_cache
---------

An implementation of an LRU cache in python.


### Example Usage
```py
lru_cache = LRUCache(2)

lru_cache.put(1, 1)  # Cache: {1: 1}
lru_cache.put(2, 2)  # Cache: {1: 1, 2: 2}
print(lru_cache.get(1))  # Returns 1, Cache order: [2, 1]
lru_cache.put(3, 3)  # Removes key 2, Cache: {1: 1, 3: 3}
print(lru_cache.get(2))  # Returns -1 (not found)
print(lru_cache.delete(1))  # Returns True, Cache: {3: 3}
print(lru_cache.get(1))  # Returns -1 (not found)
lru_cache.reset()  # Cache cleared
print(lru_cache.get(3))  # Returns -1 (not found)
lru_cache.put(4, 4)  # Cache: {4: 4}
print(lru_cache.get(4))  # Returns 4
```
