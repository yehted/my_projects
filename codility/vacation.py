A = [1, 1, 0, 1, 0, 0, 1, 1]

def solution(A):
    sea = 0
    mountains = 0
    result = 0
    total_mountains = sum(A)

    import ipdb; ipdb.set_trace()
    for i, day in enumerate(A):
        if day == 0:
            sea += 1
        else:
            mountains += 1

        if sea / (i + 1.0) > 0.5 and mountains / (i + 1.0) > 0.5:
            result += i

    return result

if __name__ == '__main__':
    print "---------------"
    print solution(A)
