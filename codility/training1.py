"""Binary Gap. Training lesson 1"""
import sys

def solution(A):
    bin_A = str(bin(A))
    print bin_A
    max_gap = 0
    gap = 0
    for i in xrange(2,len(bin_A)):
        if bin_A[i] == '1':
            gap = 0
            j = i + 1
            while j < len(bin_A) and bin_A[j] != '1':
                if bin_A[j] == '0':
                    gap += 1
                if j == len(bin_A) - 1:
                    gap = 0
                    break
                j += 1
            if gap > max_gap:
                max_gap = gap

    return max_gap


if __name__ == '__main__':
    A = sys.argv[1]
    print solution(int(A))
