import argparse

class ShorterSuperSum(object):
    @staticmethod
    def recurse(k, n):
        if k == 0:
            return n
        return sum(ShorterSuperSum.recurse(k - 1, i) for i in xrange(1, n + 1))

    @staticmethod
    def calculate(k, n):
        res = [i for i in xrange(1, n + 1)]
        for i in xrange(k):
            copy_res = res[:]
            for j in xrange(1, n + 1):
                copy_res[j - 1] = sum(res[:j])
            res = copy_res
            print res

        return res[-1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("k")
    parser.add_argument("n")
    args = parser.parse_args()
    answer = ShorterSuperSum.calculate(int(args.k), int(args.n))
    print answer
