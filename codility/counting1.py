"""
Find the earliest time at which a frog can cross a river of width X. 'A' is the
array of time. A[i] specifies the positing in the river when a leaf falls. Find
the earliest time at which a path from 1 to X is created
"""
A = [1, 3, 1, 4, 2, 3, 5, 4]
def solution(X, A):
    count = set(range(1, X + 1))
    for i, key in enumerate(A):
        try:
            count.remove(key)
        except KeyError:
            continue
        if len(count) == 0:
            return i

    return -1

if __name__ == '__main__':
    print solution(5, A)
