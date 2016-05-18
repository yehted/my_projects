import sys

A = [2, 3, 1, 5]
def solution(A):
    len_a = len(A)
    a_set = set(xrange(1, len_a + 2))
    for i in A:
        a_set.remove(i)
    return a_set.pop()

if __name__ == '__main__':
    print solution(A)
