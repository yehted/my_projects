A = [0,1,0,1,1]
A = [0, 1]
A = [0,0,1,0,1,1]

def solution(A):
    sum_a = sum(A)
    front = 0
    total = 0
    for i in xrange(len(A)):
        front += A[i]
        if A[i] == 0:
            total += (sum_a - front)
        if total > 1E9:
            return -1

    return total


if __name__ == '__main__':
    print solution(A)
