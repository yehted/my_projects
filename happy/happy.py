import sys

def _calculate(num):
    x = num
    total = 0
    while (x  > 0):
        total += (x % 10)**2
        x = x / 10
    return total

def is_happy(num):
    happy = {num: None, 1: None}
    initial = num
    while num not in happy:
        x = _calculate(num)
        if x == 1:
            return True
        happy[x] = None


def main():
    N = int(sys.argv[1])
    total = 0
    happy = [False] * N
    for initial in range(N):
        x = initial
        while not happy[x]:
            num = _calculate(x)
            if num == 1:
                print 'happy number! ', initial
                total += 1
                happy = [False] * N
                break
            happy[x] = True
            x = num

    print total, "happy numbers"

if __name__ == '__main__':
    main()