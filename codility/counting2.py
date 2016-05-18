"""
PermCheck. Checks if an array is a permutation. An array A of length N is a
permutation if and only if every integer from 1 to N appears once and only
once.
"""
def solution(A):
    # write your code in Python 2.7
    N = len(A)
    n_set = set(range(1, N+1))
    for i in A:
        try:
            n_set.remove(i)
        except KeyError:
            return 0

    if len(n_set) == 0:
        return 1
    else:
        return 0
