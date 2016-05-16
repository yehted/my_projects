A = [-1, 3, -4, 5, 1, -6, 2, 1]
def solution(A):
    Asum = sum(A)
    front = 0
    for i in range(1, len(A)):
        front += A[i - 1]
        # front = sum(A[:i])
        # back = sum(A[i+1:])
        back = Asum - front - A[i]
    #    print front
    #    print back
    #    print "---------------------"
        if back == front:
            return i
    return -1

if __name__ == '__main__':
    print solution(A)
