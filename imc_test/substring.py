# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import re

def solution(S):
    # write your code in Python 2.7
    valid = re.compile('[a-z]')
    upper = re.compile('[A-Z]')
    foo = [0] * len(S)
    has_upper = [False] * len(S)
    k = 0
    maxlen = 0

    for i in S:
        if re.match(valid, i):
            maxlen += 1
            foo[k] = max(foo[k-1], maxlen)
        elif re.match(upper, i):
            has_upper[k] = True
            maxlen += 1
            foo[k] = max(foo[k-1], maxlen)
        else:
            foo[k] = foo[k-1]
            maxlen = 0
            has_upper[k] = False

        k += 1

    return foo[-1]
