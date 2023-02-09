class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # key : Node
        self.cache = {}
        # Double linked list
        self.left = Node(0,0)
        self.right = Node(0,0)

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass