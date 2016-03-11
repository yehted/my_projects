import sys

def make_change(amount, coin_list):
    sorted_coins = sorted(coin_list, reverse=True)
    int_sorted_coins = [int(i*100) for i in sorted_coins]
    int_amount = int(amount*100)
    coin_dict = {coin: 0 for coin in int_sorted_coins}

    print int_amount
    print int_sorted_coins

    # Incrementally decrease until you can divide by coins that you have
    while int_amount > 0:
        for coin in int_sorted_coins:
            while int_amount % coin == 0:
                int_amount -= coin
                coin_dict[coin] += 1

    # Minimize the number of pennies?





def find_factors(target):
    factor_set = set()
    num = 2
    while target > (num * 2):
        if target % num == 0:
            factor_set.add(num)
            factor_set.add(target / num)
        num += 1

    return factor_set

if __name__ == '__main__':
    num = int(sys.argv[1])
    print(find_factors(num))

