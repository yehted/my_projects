class Deque(object):
    """Implements a double ended queue using linked lists"""

    class _Node(object):
        """Node class for linked list"""
        def __init__(self, _item=None, _next=None, _prev=None):
            self._item = _item
            self._next = _next
            self._prev = _prev

    def __init__(self):
        """Construct an empty deque"""
        self._first = None
        self._last = None
        self._N = 0

    def __iter__(self):
        return DequeIterator(self._first)

    def isEmpty(self):
        """is the deque empty?"""
        return self._N == 0

    def size(self):
        """return the number of items on the deque"""
        return self._N

    def addFirst(self, item):
        """add the item to the front"""
        if item == None:
            raise RuntimeError("Item is null")

        newNode = Deque._Node(item, _next=self._first)
        if self.isEmpty():
            self._last = newNode
        else:
            self._first._prev = newNode
        self._first = newNode
        self._N += 1

    def addLast(self, item):
        """add the item to the end"""
        if item == None:
            raise RuntimeError("Item is null")

        newNode = Deque._Node(item, _prev=self._last)
        if self.isEmpty():
            self._first = newNode
        else:
            self._last._next = newNode
        self._last = newNode
        self._N += 1

    def removeFirst(self):
        """remove and return the item from the front"""
        if self.isEmpty():
            raise RuntimeError("Deque is empty")

        item = self._first._item
        temp = self._first._next
        self._first._item = None
        self._first = temp
        self._N -= 1

        if self.isEmpty():
            self._last = None
        else:
            self._first._prev = None
        return item

    def removeLast(self):
        """remove and return the item from the end"""
        if self.isEmpty():
            raise RuntimeError("Deque is empty")

        item = self._last._item
        temp = self._last._prev
        self._last._item = None
        self._last = temp
        self._N -= 1

        if self.isEmpty():
            self._first = None
        else:
            self._last._next = None
        return item

    def clear(self):
        """Empties the deque"""
        while self._first != None:
            current = self._first
            self._first = self._first._next
            current._item = None
            self._N -= 1
        self._last = None
        assert self._N == 0

class DequeIterator(object):
    """Iterator for Deque"""

    def __init__(self, node):
        self._current = node

    def __iter__(self):
        return self

    def next(self):
        if self._current == None:
            raise StopIteration()

        item = self._current._item
        self._current = self._current._next

        return item

class Queue(object):
    """FIFO container built upon Deque"""

    def __init__(self):
        self._q = Deque()

    def __iter__(self):
        return DequeIterator(self._q._first)

    def put(self, item):
        self._q.addFirst(item)

    def get(self):
        return self._q.removeLast()

    def isEmpty(self):
        return self._q.isEmpty()

    def size(self):
        return self._q.size()

class Stack(object):
    """LIFO container built upon Deque"""

    def __init__(self):
        self._s = Deque()

    def __iter__(self):
        return DequeIterator(self._s._first)

    def push(self, item):
        self._s.addFirst(item)

    def pop(self):
        return self._s.removeFirst()

    def isEmpty(self):
        return self._s.isEmpty()

    def size(self):
        return self._s.size()

def main():
    """Unit tests"""
    q = Queue()
    for i in range(10):
        q.put(i)

    while not q.isEmpty():
        print q.get()

    print

    s = Stack()
    for i in range(10):
        s.push(i)

    while not s.isEmpty():
        print s.pop()

if __name__ == '__main__':
    main()
