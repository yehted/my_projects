import random

class RandomizedQueue(object):
    """a container where the item removed is chosen uniformly at random"""

    def __init__(self):
        """construct an empty randomized queue"""
        self._N = 0
        self._a = []

    def __iter__(self):
        """returns an iterator"""
        return RQIterator(self._a)

    def isEmpty(self):
        """is the queue empty?"""
        return self._N == 0

    def size(self):
        """return the number of items on the queue"""
        return self._N

    def enqueue(self, item):
        """add the item"""
        if item == None:
            raise RuntimeError("Item is null")

        self._a.append(item)
        self._N += 1

    def dequeue(self):
        """remove and return a random item"""
        if self.isEmpty():
            raise RuntimeError("Queue is empty")

        x = random.randint(0, self._N-1)
        result = self._a[x]
        self._N -= 1
        self._a[x] = self._a[self._N]
        del self._a[self._N]
        return result

    def sample(self):
        """return (but do not remove) a random item"""
        if self.isEmpty():
            raise RuntimeError("Queue is empty")

        x = random.randint(0, self._N-1)
        return self._a[x]

class RQIterator(object):
    """RandomizedQueue iterator class"""
    def __init__(self, a):
        self._a = a
        self._i = len(a)
        self._copy = []
        for j in xrange(self._i):
            self._copy.append(j)
        random.shuffle(self._copy)

    def __iter__(self):
        return self

    def next(self):
        if self._i == 0:
            raise StopIteration()

        self._i -= 1
        return self._a[self._copy[self._i]]

def main():
    """Unit Tests"""
    rq = RandomizedQueue()
    for i in "Hello World!":
        rq.enqueue(i)
    print list(rq)

    while not rq.isEmpty():
        print rq.dequeue()

if __name__ == '__main__':
    main()