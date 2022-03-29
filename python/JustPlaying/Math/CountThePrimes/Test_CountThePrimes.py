import unittest
from CountThePrimes import is_divisible_by, total_primes, is_prime


class IsDivisibleByTests(unittest.TestCase):
    def test_negative_number(self):
        self.assertRaises(ValueError, is_divisible_by, -1, 1)

    def test_negative_number_2(self):
        self.assertRaises(ValueError, is_divisible_by, 1, -1)

    def test_same_number(self):
        self.assertEqual(is_divisible_by(1, 1), True)

    def test_different_numbers(self):
        self.assertEqual(is_divisible_by(2, 1), True)

    def test_different_numbers_2(self):
        self.assertEqual(is_divisible_by(10, 5), True)

    def test_different_numbers_3(self):
        self.assertEqual(is_divisible_by(100, 3), False)


class IsPrimeNumberTests(unittest.TestCase):
    def test_is_negative_number_prime(self):
        self.assertEqual(is_prime(-1), False)

    def test_is_one_prime(self):
        self.assertEqual(is_prime(1), False)

    def test_is_three_prime(self):
        self.assertEqual(is_prime(3), True)

    def test_is_five_prime(self):
        self.assertEqual(is_prime(5), True)

    def test_is_7_prime(self):
        self.assertEqual(is_prime(7), True)

    def test_is_50_prime(self):
        self.assertEqual(is_prime(50), False)


class CountThePrimes(unittest.TestCase):
    def test_primes_of_negative(self):
        self.assertEqual(total_primes(-1), 0)

    def test_primes_of_negative_2(self):
        self.assertEqual(total_primes(-100), 0)

    def test_primes_of_1(self):
        self.assertEqual(total_primes(1), 0)

    def test_primes_of_2(self):
        self.assertEqual(total_primes(2), 1)

    def test_primes_of_3(self):
        self.assertEqual(total_primes(3), 2)

    def test_primes_of_7(self):
        self.assertEqual(total_primes(7), 4)

    def test_primes_of_100(self):
        self.assertEqual(total_primes(100), 25)

    def test_primes_of_1000(self):
        self.assertEqual(total_primes(1000), 168)

    def test_primes_of_10000(self):
        self.assertEqual(total_primes(10000), 1229)


if __name__ == '__main__':
    unittest.main()
