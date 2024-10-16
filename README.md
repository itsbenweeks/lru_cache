lru_cache
---------

An implementation of an LRU cache in python.


### Example Usage
```py
lru_cache = LRUCache(2)

lru_cache[1] = 'A'  # Cache: {1: 'A'}
lru_cache[2] = 'B'  # Cache: {1: 'A', 2: 'B'}
print(lru_cache[1])  # Returns 'A', Cache order: [2, 1]
lru_cache[3] = 'C'  # Removes key 2, Cache: {1: 'A', 3: 'C'}
try:
    print(lru_cache[2])  # Raises KeyError
except KeyError:
    print("Key 2 not found.")
lru_cache[4] = 'D'  # Removes key 1, Cache: {3: 'C', 4: 'D'}
try:
    print(lru_cache[1])  # Raises KeyError
except KeyError:
    print("Key 1 not found.")
print(lru_cache[3])  # Returns 'C', Cache order: [4, 3]
print(lru_cache[4])  # Returns 'D'
lru_cache.reset()  # Clears the cache
print(len(lru_cache))  # Returns 0
```
