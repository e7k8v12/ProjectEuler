# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
#
# 6857


class PrimeNumbers:
    def __init__(self):
        self.current = 2
        self.primes = []

    def _is_prime(self):
        for i in self.primes:
            if i * i > self.current:
                break
            if self.current % i == 0:
                return False
        self.primes.append(self.current)
        return True

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 3:
            self.current += 1
            return self.current - 1
        while not self._is_prime():
            self.current += 2
        self.current += 2
        return self.current - 2

    def first(self):
        self.current = 2


def get_dividers(num):
    dividers = []
    primes = PrimeNumbers()
    while num != 1:
        primes.first()
        for i in primes:
            if num % i == 0:
                dividers.append(i)
                num /= i
                break
    return dividers

print(get_dividers(600851475143)[-1])
