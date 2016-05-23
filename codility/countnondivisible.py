from math import sqrt
A = [15, 168, 3]
B = [75, 84, 5]

def sieve(N):
    arr = [True] * (N + 1)
    arr[0] = False
    arr[1] = False

    i = 2
    primes = []
    while (i * i <= N):
        if arr[i]:
            k = i * i
            while k <= N:
                arr[k] = False
                k += i
        i += 1

    return arr

def get_primes(N, primes):
    my_primes = []
    i = 2
    for i in primes:
        if N % i == 0:
            my_primes.append(i)

    return my_primes

def solution(A, B):
    N = len(A)
    both = A + B
    biggest = int(sqrt(max(both)))
    prime_array = sieve(biggest)
    primes = [i for i, isprime in enumerate(prime_array) if isprime]
    print primes
    result = 0
    print biggest
    for i in xrange(N):
        Aprimes = get_primes(A[i], primes)
        Bprimes = get_primes(B[i], primes)
        print Aprimes
        print Bprimes
        if set(Aprimes) == set(Bprimes):
            result += 1

    return result

if __name__ == '__main__':
    print solution(A, B)
