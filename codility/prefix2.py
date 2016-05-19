
def solution(A, B, K):
    # write your code in Python 2.7
    top = B / K
    if A % K == 0:
        bottom = A / K
    else:
        bottom = A / K + 1

    return top - bottom + 1

if __name__ == '__main__':
    print solution(6, 11, 2)
    print solution(1, 100, 10)
    print solution(10, 100, 10)
    print solution(11, 100, 10)
    print solution(20, 100, 10)
    print solution(9, 100, 10)
    print solution(1, 101, 10)
    print solution(10, 101, 10)
    print solution(19, 101, 10)
