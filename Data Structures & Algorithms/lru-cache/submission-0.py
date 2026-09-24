class ListNode():
    def __init__(self, key=0, val = 0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        temp = self.tail.prev
        temp.nxt = node
        node.nxt = self.tail
        self.tail.prev = node
        node.prev = temp
        self.m[node.key] = node

    def remove(self,node):
        temp = node.prev
        temp.nxt = node.nxt
        node.nxt.prev = temp
        del self.m[node.key]

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        if self.tail.prev!=self.m[key]:
            node = self.m[key]
            self.remove(node)
            self.insert(node)
            self.m[key] = node
        return self.m[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            node = self.m[key]
            node.val = value
            self.remove(node)
            self.insert(node)
            self.m[key] = node
            return 
        if len(self.m)==self.capacity:
            self.remove(self.head.nxt)
        self.insert(ListNode(key,value))