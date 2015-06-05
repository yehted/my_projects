import numpy
import WeightedQuickUnionUF as wf

class Percolation(object):
    """Percolation class, with convention that an N-by-N grid is indexed from
    1 to N^2
    """

    def __init__(self, N):
        """Create N-by-N grid, with all sites blocked

        A system percolates when the top virtual node is connected with
        the bottom virtual node. Two WeightedQuickUnionUF objects are needed
        for the visualization simulation in order to prevent backwash.
        """
        self._gridSize = N
        self._grid = wf.WeightedQuickUnionUF(N*N + 2)
        self._grid2 = wf.WeightedQuickUnionUF(N*N + 1)
        self._bottom = N*N + 1
        self._site = numpy.zeros(N*N + 1, dtype = numpy.bool)

    def _xyTo1D(self, i, j):
        """Converts (i, j) coordinates to 1D vector index"""
        return self._gridSize * (i - 1) + j

    def _isValidIndex(self, i, j):
        """Checks if (i, j) is a valid coordinate"""
        return ((i > 0 and i <= self._gridSize) and
            (j > 0 and j <= self._gridSize))

    # def _isConnected(self, i, j):
    #     """Checks if i and j are connected"""
    #     return self._grid.connected(i, j)

    def open(self, i, j):
        """Open site (row i, column j) if it is not open already"""
        if not self._isValidIndex(i,j):
            raise IndexError("Index out of bounds")

        idx = self._xyTo1D(i, j)
        self._site[idx] = True

        if self._isValidIndex(i-1, j) and self.isOpen(i-1, j):
            self._grid.unite(idx, self._xyTo1D(i-1, j))
            self._grid2.unite(idx, self._xyTo1D(i-1, j))

        if self._isValidIndex(i+1, j) and self.isOpen(i+1, j):
            self._grid.unite(idx, self._xyTo1D(i+1, j))
            self._grid2.unite(idx, self._xyTo1D(i+1, j))

        if self._isValidIndex(i, j-1) and self.isOpen(i, j-1):
            self._grid.unite(idx, self._xyTo1D(i, j-1))
            self._grid2.unite(idx, self._xyTo1D(i, j-1))

        if self._isValidIndex(i, j+1) and self.isOpen(i, j+1):
            self._grid.unite(idx, self._xyTo1D(i, j+1))
            self._grid2.unite(idx, self._xyTo1D(i, j+1))

        if (i == 1):
            self._grid.unite(0, idx)
            self._grid2.unite(0, idx)

        if (i == self._gridSize):
            self._grid.unite(idx, self._bottom)

    def isOpen(self, i, j):
        """is site (row i, column j) open?"""
        if not self._isValidIndex(i, j):
            raise NameError("Index out of range")

        return self._site[self._xyTo1D(i, j)]

    def isFull(self, i, j):
        """is site (row i, column j) full?"""
        if not self.isOpen(i, j): return False
        idx = self._xyTo1D(i, j)
        return (self._grid2.connected(idx, 0))

    def percolates(self):
        """Does the system percolate?"""
        return self._grid.connected(self._bottom, 0)

def main():
    """Unit tests for Percolation class"""
    N = int(raw_input("Input size of grid: "))
    pc = Percolation(N)
    while True:
        p = raw_input()
        if not p: break
        p = int(p)
        q = int(raw_input())

if __name__ == '__main__':
    main()