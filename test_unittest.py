from lru_cache import LRUCache

def test_max_size():
    lruCache = LRUCache(3)
    assert lruCache.maxSize == 3

def test_put():
    lruCache = LRUCache(3)
    for i in [5,2,5,2,1,4,6,8,3,0,1,4,6]:
        lruCache.put(i, i)
    assert lruCache.get(1) == 1
    assert lruCache.get(4) == 4
    assert lruCache.get(6) == 6
    assert lruCache.get(2) == -1
    assert lruCache.length == 3

def test_dll():
    lruCache = LRUCache(3)
    for i in [5,2,5,1]:
        lruCache.put(i, i)
    assert lruCache.tail.key == 1
    assert lruCache.tail.prev.key == 5
    assert lruCache.tail.prev.prev.key == 2
    assert lruCache.length == 3
    assert lruCache.head.next.key == 2
    assert lruCache.head.next.next.key == 5
    assert lruCache.head.next.next.next.key == 1
    assert lruCache.head.next.next.next.next == None

def test_get():
    lruCache = LRUCache(3)
    lruCache.put(1, 3)
    lruCache.get(1)
    assert lruCache.get(1) == 3

def test_delete():
    lruCache = LRUCache(3)
    for i in [5,2,5,2,1,4,6,8,3,0,1,4,6]:
        lruCache.put(i, i)
    assert lruCache.length == 3
    assert lruCache.get(1) == 1
    assert lruCache.get(4) == 4
    assert lruCache.get(6) == 6

    lruCache.delete(6)
    assert lruCache.get(6) == -1
    assert lruCache.length == 2


def test_reset():
    lruCache = LRUCache(3)
    for i in [5,2,5,2,1,4,6,8,3,0,1,4,6]:
        lruCache.put(i, i)
    assert lruCache.length == 3
    lruCache.reset()
    assert lruCache.length == 0
    assert lruCache.head.val == -1
    assert lruCache.hash == {}
    assert lruCache.maxSize == 3