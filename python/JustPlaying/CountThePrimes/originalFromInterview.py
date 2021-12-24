# Given the number N return the total number primes up to and including N
DEBUG = False

def total_primes(input_number: int) -> int:
    """
        Numbers below 0 return 0
        Given the number N return the total number primes up to and including N
    """
    if input_number <= 1:
        return 0
    if input_number == 2:
        return 1
    primes = 1
    for n in range(3, input_number+1, 2):
        if DEBUG:
            print("n", n)
        divisors = 0
        for internal_iterator in range(2, n+1):
            if DEBUG:
                print("internal_iterator", internal_iterator, internal_iterator == input_number)
            # if internal_iterator == n and divisors == 0:
            #     primes = primes + 1
            if n % internal_iterator > 0:
                divisors = divisors + 1
        if divisors > 0:
            primes = primes + 1
    return primes

print("n=-1", total_primes(-1))
print("n=1", total_primes(1))
print("n=2", total_primes(2))
print("n=3", total_primes(3))
print("n=7", total_primes(7))