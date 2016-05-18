"""Codility lessoon 2 in arrays: oddone out"""

A = [9,3,9,3,9,7,9]
B = [9,3,3,7,9,9,9]

def solution(A):
    foo = {}
    for i in A:
        if i in foo:
            if foo[i] == 1:
                foo.pop(i)
            else:
                foo[i] -= 1
        else:
            foo[i] = 1

    return foo.keys()[0]

if __name__ == '__main__':
    print solution(B)
