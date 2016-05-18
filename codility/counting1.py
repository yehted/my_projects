import sys

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
