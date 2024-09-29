class Node:
    def __init__(self, f: int):
        self.freq = f
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.map = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        cur = self.head
        newF = 1
        if key in self.map:
            cur = self.map[key]
            newF = cur.freq + 1
            cur.keys.remove(key)
        
        if cur.next.freq == newF:
            cur.next.keys.add(key)
        else:
            node = Node(newF)
            node.keys.add(key)
            node.next = cur.next
            cur.next.prev = node
            cur.next = node
            node.prev = cur

        self.map[key] = cur.next
        
        if len(cur.keys) == 0 and cur != self.head:
            self._removeNode(cur)

    def dec(self, key: str) -> None:
        cur = self.map[key]
        freq = cur.freq - 1
        cur.keys.remove(key)

        if freq == 0:
            if len(cur.keys) == 0:
                self._removeNode(cur)
            del self.map[key]
            return

        if cur.prev.freq == freq:
            cur.prev.keys.add(key)
        else:
            node = Node(freq)
            node.keys.add(key)
            node.prev = cur.prev
            cur.prev.next = node
            node.next = cur
            cur.prev = node
        
        self.map[key] = cur.prev

        if len(cur.keys) == 0 and cur != self.head:
            self._removeNode(cur)

    def getMaxKey(self) -> str:
        if self.head == self.tail.prev:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

    def _removeNode(self, cur: Node):
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        cur.next = None
        cur.prev = None
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
