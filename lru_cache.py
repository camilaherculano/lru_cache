from dll import DLL

class LRUCache:
    
    def __init__(self, maxSize: int):
        self.head = DLL(-1,-1)
        self.tail = self.head
        self.hash = {}
        self.maxSize = maxSize
        self.length = 0
        
    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        node = self.hash[key]
        val = node.val
        while node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        return val
        
    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            node.val = value
            while node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
        else:
            node = DLL(key, value)
            self.hash[key] = node
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.length += 1
            if self.length > self.maxSize:
                remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.hash[remove.key]
                self.length -= 1
                
    def delete(self, key: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
            del self.hash[node.key]
            self.length -= 1
        
    def reset(self) -> None:
        self.head = DLL(-1,-1)
        self.tail = self.head
        self.hash = {}
        self.length = 0
