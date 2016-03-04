import numpy as np
cimport numpy as np
import cython
from cython.parallel cimport prange

@cython.boundscheck(False)
def julia_cython(int N):
    cdef np.ndarray[np.uint8_t, ndim=2] T = np.empty((N, 2*N), dtype=np.uint8)
    # cdef double complex c = -0.835 - 0.2321j
    cdef double complex c = -0.74543 + 0.11301j
    cdef double complex z
    cdef int J, I
    cdef double h = 2.0/N
    cdef double x, y
    for J in prange(N, nogil=True, schedule="guided"):
        for I in xrange(2*N):
            y = -1.0 + J*h
            x = -2.0 + I*h
            T[J,I] = 0
            z = x + 1j * y
            while z.imag**2 + z.real**2 <= 4:
                z = z**2 + c
                T[J,I] += 1

    return T
