def solution(A):
    # write your code in Python 2.7
    N = len(A)
    a_set = set(A)
    for i in xrange(1, N + 1):
        if i not in a_set:
            return i

    return N + 1
