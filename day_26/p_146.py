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
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        leftNode = node.prev
        rightNode = node.next
        leftNode.next = rightNode
        rightNode.prev = leftNode

    def insert(self, node):
        

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass