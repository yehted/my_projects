import sys

def solution(X, Y, D):
    distance = Y - X
    if distance % D == 0:
        return distance / D
    else:
        return distance / D + 1


if __name__ == '__main__':
    X = int(sys.argv[1])
    Y = int(sys.argv[2])
    D = int(sys.argv[3])

    print solution(X, Y, D)
