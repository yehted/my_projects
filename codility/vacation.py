A = [1, 1, 0, 1, 0, 0, 1, 1]
B = [1, 1, 1, 0, 1, 0, 1, 0]


def calculate(start, middle, end, A):
    len_sea = middle - start + 0.0
    len_mountains = end - middle + 0.0
    total_mountains = sum(A)
    sea = sum(A[start:middle]) / len_sea
    mountains = sum(A[middle + 1: end + 1]) / len_mountains

    return sea, mountains

def solution(A):
    print A
    sea = 0
    mountains = 0
    result = 0
    sum_A = sum(A)

    start = 0
    end = len(A) - 1
    middle = 1

    front = 0.0
    while start != middle and end != middle + 1:
        front += A[middle]
        if front / sum_A >= 0.5:
            start += 1
        if (sum_A - front) / sum_A < 0.5:
            end -= 1
        if front < sum_A:
            middle += 1
        else:
            middle -= 1

    print "---------------"
    print A[start:end + 1]
    return end - start + 1

if __name__ == '__main__':
    print solution(A)
