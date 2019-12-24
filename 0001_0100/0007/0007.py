# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
# Какое число является 10001-ым простым числом?
#
# 104743


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


number_number = 10001
primes = PrimeNumbers()
for i, j in enumerate(primes):
    if i == number_number - 1:
        break

print(j)