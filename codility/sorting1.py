import random

A = [10, 2, 5, 1, 8, 20]
A = [10, 50, 5, 1]

def solution(A):
    A.sort()
    print A
    N = len(A)
    for i in xrange(N-2):
        if (A[i] + A[i+1] > A[i+2]):
            return 1

    return 0

if __name__ == '__main__':
    foo = [random.randint(1,100) for i in xrange(6)]
    print foo
    print solution([5,3,3])
