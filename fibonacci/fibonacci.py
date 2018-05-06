import sys

def main(N):
    a = 0
    b = 1
    for _ in xrange(N):
        yield a
        tmp = a # save a for later
        a = b # increment a to b
        b = a + tmp # increment b to itself plus the one before



if __name__ == '__main__':
    g = main(int(sys.argv[1]))
    print list(g)
