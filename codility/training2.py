"""Rotating an array"""
import sys

A = [3, 8, 9, 7, 6]

def solution(A, K):
    N = len(A)
    result = [0] * N
    for i in xrange(N):
        v = i + K
        if v >= N:
            v %= N
        result[v] = A[i]

    return result


if __name__ == '__main__':
    K = int(sys.argv[1])
    print solution(A, K)
