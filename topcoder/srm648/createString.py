import argparse

class AB(object):
    @staticmethod
    def createString(N, K):
        result = ""
        if N < K:
            return result
        count = 0
        result += 'A'
        while len(result) < N:
            if count < K:
                result += 'B'
            else:
                result = 'B' + result
        return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("N")
    parser.add_argument("K")
    args = parser.parse_args()
    answer = AB.createString(int(args.N), int(args.K))
    print answer