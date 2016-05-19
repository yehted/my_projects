
P = [2, 5, 0]
Q = [4, 5, 6]

def solution(S, P, Q):
    # write your code in Python 2.7
    N = len(S)

    matrix = {
        "A": [0] * (N + 1),
        "C": [0] * (N + 1),
        "G": [0] * (N + 1),
        "T": [0] * (N + 1),
    }

    # Populate matrix
    for i in xrange(N):
        matrix[S[i]][i+1] = 1
    print matrix

    # Calculate prefixes (i.e. at any given time, how many of each letter has
    # shown up already)
    for i in xrange(1, N + 1):
        for value in matrix.values():
            value[i] += value[i-1]
    print matrix

    # Calculate minimum in range
    result = [0] * len(P)
    for i in xrange(len(P)):
        if matrix["A"][Q[i]+1] > matrix["A"][P[i]]:
            result[i] = 1
        elif matrix["C"][Q[i]+1] > matrix["C"][P[i]]:
            result[i] = 2
        elif matrix["G"][Q[i]+1] > matrix["G"][P[i]]:
            result[i] = 3
        elif matrix["T"][Q[i]+1] > matrix["T"][P[i]]:
            result[i] = 4

    return result

if __name__ == '__main__':
    print solution("CAGCCTA", P, Q)
    print solution("GATTACA", P, Q)
    # print solution("GTATTGACCAGCCTA", [3,6,0], [5,7,7])
