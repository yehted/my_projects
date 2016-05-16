"""
An equilibrium index is the index where all the previous values of the list add
up to the sum of all the subsequent values of the list. In the example list A
given below, equilibrium indices are at 1, 3, and 7
"""
A = [-1, 3, -4, 5, 1, -6, 2, 1]
def solution(A):
    result = [-1] * (len(A) + 1)
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
#        if back == front:
#            return i
        result[i] = front == back
    return result

if __name__ == '__main__':
    print solution(A)
