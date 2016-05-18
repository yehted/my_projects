import sys
A = [3, 1, 2, 4, 3]

def solution(A):
    sum_A = sum(A)
    front = A[0]
    mingap = sys.maxint
    for i in xrange(1, len(A)):
        back = sum_A - front
        gap = abs(back - front)
        print front, back, gap
        if gap < mingap:
            mingap = gap
        front += A[i]

    return mingap

if __name__ == '__main__':
    print solution(A)
