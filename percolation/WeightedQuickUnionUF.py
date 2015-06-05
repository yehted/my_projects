import numpy
from ns_core import exceptions

class WeightedQuickUnionUF(object):
    """Weighted Quick Union Union-Find class"""

    def __init__(self, N):
        """Initializes an empty union-find data structure
        with N isolated components 0 through N-1
        """
        self._count = N
        try:
            self._id = numpy.arange(N)
            self._sz = numpy.ones(N, dtype = numpy.int)
        except (TypeError, ValueError):
            raise exceptions.DataValidationError("Positive integer expected")

    def count(self):
        """Returns the number of components"""
        return self._count

    def find(self, p):
        """Returns the component identifier for the component on site p"""
        while (p != self._id[p]):
            p = self._id[p]
        return p

    def connected(self, p, q):
        """Are the two sites in the same component?"""
        return self.find(p) == self.find(q)

    def unite(self, p, q):
        """Merges the component containing p with the component containing q"""
        rootP = self.find(p)
        rootQ = self.find(q)
        if (rootP == rootQ):
            return

        # Make smaller root point to larger ones
        if (self._sz[rootP] < self._sz[rootQ]):
            self._id[rootP] = rootQ
            self._sz[rootQ] += self._sz[rootP]
        else:
            self._id[rootQ] = rootP
            self._sz[rootP] += self._sz[rootQ]

def main():
    """Reads in a sequence of pairs of integers from standard input

    Where each integer represents some object;
    if the objects are in different components, merge the two components
    and print the pair to standard output.
    """
    N = int(raw_input("Input N: "))
    uf = WeightedQuickUnionUF(N)
    while True:
        p = raw_input()
        if not p: break
        p = int(p)
        q = int(raw_input())
        if (uf.connected(p, q)): continue
        uf.unite(p, q)
        print p, q
    print uf.count, "components"

if __name__ == '__main__': main()