import numpy
import WeightedQuickUnionUF as wf

class Percolation3D(object):
    """3D Percolation class, with convention that an N-by-N-by-N grid
    is indexed from 1 to N^3
    """

    def __init__(self, N):
        """Create N-by-N-by-N grid, with all sites blocked

        A system percolates when the top virtual node is connected with
        the bottom virtual node. Two WeightedQuickUnionUF objects are needed
        for the visualization simulation in order to prevent backwash.
        """
        self._gridSize = N
        self._grid = wf.WeightedQuickUnionUF(N**3 + 2)

        self._bottom = N**3 + 1
        #self._site = numpy.zeros(N**3 + 1, dtype = numpy.bool)
        self._site = numpy.zeros(shape=(N,N,N), dtype=numpy.bool)

    def _xyzTo1D(self, i, j, k):
        """Converts (i, j) coordinates to 1D vector index"""
        return (k - 1) * self._gridSize**2 + self._gridSize * (i - 1) + j

    def _isValidIndex(self, i, j, k):
        """Checks if (i, j) is a valid coordinate"""
        return ((i > 0 and i <= self._gridSize) and \
            (j > 0 and j <= self._gridSize)) and \
            (k > 0 and k <= self._gridSize)

    def open(self, i, j, k):
        """Open site (row i, column j, k) if it is not open already"""
        if not self._isValidIndex(i, j, k):
            raise IndexError("Index out of bounds")

        idx = self._xyzTo1D(i, j, k)
        self._site[i-1, j-1, k-1] = True

        for x, y, z in [(i-1, j, k), (i+1, j, k),
            (i, j-1, k), (i, j+1, k),
            (i, j, k-1), (i, j, k+1)]:
            if self._isValidIndex(x, y, z) and self.is_open(x, y, z):
                self._grid.unite(idx, self._xyzTo1D(x, y, z))

        if (k == 1):
            self._grid.unite(0, idx)

        if (k == self._gridSize):
            self._grid.unite(idx, self._bottom)

    def is_open(self, i, j, k):
        """is site (row i, column j) open?"""
        if not self._isValidIndex(i, j, k):
            raise NameError("Index out of range")

        return self._site[i-1, j-1, k-1]

    def percolates(self):
        """Does the system percolate?"""
        return self._grid.connected(self._bottom, 0)

def main():
    """Unit tests for Percolation class"""
    N = int(raw_input("Input size of grid: "))
    pc = Percolation3D(N)
    while True:
        p = raw_input()
        if not p: break
        p = int(p)
        q = int(raw_input())

if __name__ == '__main__':
    main()