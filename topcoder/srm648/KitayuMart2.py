import argparse

class KitayuMart2(object):
    @staticmethod
    def numBought(K, T):
        total = 0
        num = 1
        while total <= T:
            total += (2**num * K)
            num += 1

        return num-1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("K")
    parser.add_argument("T")
    args = parser.parse_args()
    KM = KitayuMart2.numBought(int(args.K), int(args.T))
    print KM