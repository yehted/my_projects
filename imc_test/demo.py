A = [-1, 3, -4, 5, 1, -6, 2, 1]
Asum = sum(A)
front = 0
for i in range(len(A)):
    front = sum(A[:i])
    # front = sum(A[:i])
    # back = sum(A[i+1:])
    back = Asum - front - A[i]
    print front
    print back
    print "---------------------"
