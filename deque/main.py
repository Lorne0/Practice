
class Node:
    def __init__(self, v: int = 0, next: 'Node' = None, prev: 'Node' = None):
        self.v = v
        self.next = next
        self.prev = prev


class QueueEmptyException(Exception):
    pass


class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def to_array(self) -> list:
        r = []
        cur = self.front
        while cur:
            r.append(cur.v)
            cur = cur.next
        return r

    def push_front(self, n: int):
        if self.is_empty():
            self.back = self.front = Node(n)

        else:
            new = Node(n)
            new.next = self.front
            self.front.prev = new
            self.front = new

        self.length += 1

    def push_back(self, n: int):
        if self.is_empty():
            self.back = self.front = Node(n)

        else:
            new = Node(n)
            new.prev = self.back
            self.back.next = new
            self.back = new

        self.length += 1

    def pop_front(self) -> int:
        if self.is_empty():
            raise QueueEmptyException('pop front')

        v = self.front.v
        tmp = self.front.next
        self.front.next = None
        tmp.prev = None
        self.front = tmp

        return v

    def pop_back(self) -> int:
        if self.is_empty():
            raise QueueEmptyException('pop back')

        v = self.back.v
        tmp = self.back.prev
        self.back.prev = None
        tmp.next = None
        self.back = tmp

        return v
