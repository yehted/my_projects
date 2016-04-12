import sys

def _make_matrix(coins, W):
    m = [[0 for _ in xrange(W + 1)] for _ in xrange(len(coins) + 1)]
    for i in xrange(W + 1):
        m[0][i] = i
    return m

def full_m(coins, W):
    min_coins = _make_matrix(coins, W)
    for c in xrange(1, len(coins) + 1):
        for value in xrange(1, W + 1):
            if coins[c - 1] == value:
                min_coins[c][value] = 1

            elif coins[c - 1] > value:
                min_coins[c][value] = min_coins[c - 1][value]

            else:
                min_coins[c][value] = min(
                    min_coins[c - 1][value], 1 + min_coins[c][value - coins[c - 1]])
    return min_coins

def short_m(coins, W):
    min_coins = [0 for _ in xrange(W + 1)]
    for value in xrange(W + 1):
        min_count = value
        for coin in [c for c in coins if c <= value]:
            if min_coins[value - coin] + 1 < min_count:
                min_count = min_coins[value - coin] + 1
        min_coins[value] = min_count

    return min_coins

if __name__ == '__main__':
    coins = [1, 5, 10, 23]
    # coins = [1, 20, 30, 51]
    num = int(sys.argv[1])
    # full_ans = full_m(coins, num)
    short_ans = short_m(coins, num)
    print short_ans
