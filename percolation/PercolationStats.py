import percolation
import numpy
from sys import argv

class PercolationStats(object):
    """Compute percolation threshold statistics of T simulations on
    N by N grids
    """

    def __init__(self, N, T):
        """Perform T independent experiments on an N by N grid"""
        if (N < 1 or T < 1):
            raise NameError("Illegal argument")

        self._results = numpy.empty(T, dtype=numpy.float)
        self._trials = T

        for x in xrange(T):
            perc = percolation.Percolation(N)
            thresh = 0
            while not perc.percolates():

                # Simulated do-while loop to find a closed site
                i = numpy.random.randint(1, N+1)
                j = numpy.random.randint(1, N+1)
                while perc.isOpen(i, j):
                    i = numpy.random.randint(1, N+1)
                    j = numpy.random.randint(1, N+1)

                perc.open(i, j)
                thresh += 1

            self._results[x] = thresh / float(N*N)

    def mean(self):
        """Sample mean of percolation threshold"""
        return numpy.mean(self._results)

    def stddev(self):
        """Sample standard deviation of percolation threshold"""
        return numpy.std(self._results)

    def confidence_lo(self):
        """low endpoint of 95% confidence interval"""
        return self.mean() - 1.96 * self.stddev() / numpy.sqrt(self._trials)

    def confidence_hi(self):
        """high endpoint of 95% confidence interval"""
        return self.mean() + 1.96 * self.stddev() / numpy.sqrt(self._trials)

def main():
    """Takes two command line arguments, N (grid size) and T (number of
    trials to run) and computes the statistics of T percolation
    simulations. Prints the mean, standard deviation, and 95% confidence
    interval.
    """
    N = int(argv[1])
    T = int(argv[2])
    test = PercolationStats(N, T)
    print "mean = ", test.mean()
    print "stddev = ", test.stddev()
    print "95% confidence interval = {lo}, {hi}".format(lo=test.confidence_lo(),
        hi=test.confidence_hi())

if __name__ == '__main__':
    main()