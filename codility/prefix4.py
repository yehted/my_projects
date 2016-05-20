import random

A = [4,2,2,5,1,5,8]


def solution(A):
    N = len(A)
    P = [0] * (N+1)
    total = 0
    for i in xrange(1,N+1):
       total += A[i-1]
       P[i] = total

    print P

    avg = [0] * (N-1)
    min_avg = P[-1]
    min_idx = N
    for j in xrange(1, N):
        temp = P[j+1] / (j + 1.0)
        avg[j-1] = temp
        if temp < min_avg:
            min_avg = temp
            min_idx = j-1

    print avg
    return min_idx

if __name__ == '__main__':
    foo = [random.randint(1,10) for i in xrange(7)]
    print foo
    print solution(foo)
