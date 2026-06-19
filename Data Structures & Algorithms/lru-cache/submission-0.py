class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev

    def move_to_tail(self, node):
        self.remove(node)
        self.insert(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        current_node = self.cache[key]
        self.move_to_tail(current_node)
        return current_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            current_node = self.cache[key]
            current_node.val = value
            self.move_to_tail(current_node)
            return

        if self.capacity == 0:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        else:
            self.capacity -= 1
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)
