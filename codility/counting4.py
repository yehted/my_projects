
A = [3,4,4,6,1,4,4]
N = 5
def solution(N, A):
    result = [0] * N
    maxcount = 0
    maxint = 0
    for i in A:
        if i == N + 1:
            maxcount = maxint
        else:
            if result[i-1] < maxcount:
                result[i-1] = maxcount
            result[i-1] += 1
            if result[i-1] > maxint:
                maxint = result[i-1]

    print maxcount
    print result
    for j in xrange(len(result)):
        if result[j] < maxcount:
            result[j] = maxcount

    return result

if __name__ == '__main__':
    print solution(N, A)
