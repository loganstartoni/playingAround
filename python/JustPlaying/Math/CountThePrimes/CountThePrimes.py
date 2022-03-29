# Given the number N return the total number primes up to and including N

# Makes more verbose and adds ability to toggle printing on and off.
DEBUG = False


def is_divisible_by(top_number: int, bottom_number: int) -> bool:
    """
    Runs the following operation and returns a boolean if the top number is divisible by the bottom number

    (top_number % bottom_number) == 0

    :param top_number: Positive Integer
    :param bottom_number: Positive Integer
    :return:
    """
    if top_number <= 0 or bottom_number <= 0:
        raise ValueError("Please ensure both numbers are positive.")

    return (top_number % bottom_number) == 0


def is_prime(number: int) -> bool:
    """
        Loops through numbers and returns if a value is prime.

    :param number: an Integer
    :return: returns if that integer is prime.
    """
    if number <= 1:
        return False
    for possible_divisor in range(2, number):
        if is_divisible_by(number, possible_divisor):
            return False
    return True


def total_primes(input_number: int) -> int:
    """
        Numbers below 0 return 0
        Given the number N return the total number primes up to and including input_number
    :param input_number: integer
    :return: Number of Primes less then or equal to input_number
    """
    if input_number <= 1:
        return 0
    if input_number == 2:
        return 1
    primes = 1
    for number_to_test in range(3, input_number+1, 2):
        if DEBUG:
            print("number_to_test", number_to_test)
        if is_prime(number_to_test):
            primes = primes + 1
    return primes
