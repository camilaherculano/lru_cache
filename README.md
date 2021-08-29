# lru_cache

LRU Cache or Least Recently Used Cache is organizes items in order of use. 

In that implementation was used a Hash for check and return, and DLL for insert and remove. All operations executes in O(1).

# Put method

Consider cache maximum capacity 3. When inserting a new key, that key is the least recently used and added in tail's DLL. If the key already exist in cache, it is just moved to the tail, because it is considered a use of that key.

# Get method

The get method receives a key, searches for it in the cache and returns its value. That operation is also considered a use of that key, so that key is moved to the tail.
If the key is not in cache, returns -1.

# Delete (del) method

That method was renamed to Delete, because del is a reserved key in Python.

This method receives a key, searches for it in the cache and removes it from DLL if it exists. 

# Reset method

This method simple resets the hash, but preserving its maximum size previously set.
