lru_cache
---------

An implementation of an LRU cache in python.


### Example Usage
```py
lru_cache = LRUCache(2)

lru_cache[1] = 1  # Cache: {1: 1}
lru_cache[2] = 2  # Cache: {1: 1, 2: 2}
print(lru_cache[1])  # Returns 1, Cache order: [2, 1]
lru_cache[3] = 3  # Removes key 2, Cache: {1: 1, 3: 3}
try:
    print(lru_cache[2])  # Raises KeyError
except KeyError:
    print("Key 2 not found.")
lru_cache[4] = 4  # Removes key 1, Cache: {3: 3, 4: 4}
try:
    print(lru_cache[1])  # Raises KeyError
except KeyError:
    print("Key 1 not found.")
print(lru_cache[3])  # Returns 3, Cache order: [4, 3]
print(lru_cache[4])  # Returns 4
lru_cache.reset()  # Clears the cache
print(len(lru_cache))  # Returns 0
```
