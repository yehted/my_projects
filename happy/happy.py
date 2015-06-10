import sys

def _calculate(num):
    x = num
    total = 0
    while (x  > 0):
        total += (x % 10)**2
        x = x / 10
    return total

def is_happy(num):
    happy = {}
    initial = num
    while num not in happy:
        happy[num] = None
        x = _calculate(num)
        if x == 1:
            return True
        num = x

    return False

def happy_range(N):
    total = 0
    happy = [False] * 10000
    for initial in xrange(N):
        x = initial
        while not happy[x]:
            num = _calculate(x)
            if num == 1:
                print 'happy number! ', initial
                total += 1
                happy = [False] * 10000
                break
            happy[x] = True
            x = num

    print total, "happy numbers"

def main():
    print "1. All the happy numbers in range"
    print "2. Is this number happy?"
    choice = raw_input("Choice: ")

    N = int(sys.argv[1])

    if choice == '1':
        happy_range(N)
    elif choice == '2':
        print is_happy(N)
    else:
        print "invalid choice"

if __name__ == '__main__':
    main()