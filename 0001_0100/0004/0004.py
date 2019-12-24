# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
#
# 913 * 993 = 906609

max_value = max_i = max_j = 0
num_of_digits = 3
for i in range(10 ** (num_of_digits-1), 10 ** num_of_digits):
    for j in range(10 ** (num_of_digits-1), 10 ** num_of_digits):
        mu = i * j
        st = str(mu)
        if st == st[::-1]:
            if max_value < mu:
                max_value = mu
                max_i = i
                max_j = j

print(str(max_i) + " * " + str(max_j) + " = " + str(max_value))
