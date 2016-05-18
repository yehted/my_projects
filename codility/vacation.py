A = [1, 1, 0, 1, 0, 0, 1, 1]

def solution(A):
    sea = 0
    mountains = 0
    result = 0

    start = 0
    end = len(A) - 1

    total_mountains = sum(A)

    while start != end:
        temp_sum = sum(A[start:end + 1])
        temp_len = end - start + 1.0

        mountains = temp_sum / temp_len
        sea = 1.0 - mountains
        print mountains, sea

        if mountains > 0.5 and sea > 0.5:
            return temp_len
        if sea <= 0.5:
            start += 1
        if mountains <= 0.5:
            end -= 1


    return 0

if __name__ == '__main__':
    print "---------------"
    print solution(A)
