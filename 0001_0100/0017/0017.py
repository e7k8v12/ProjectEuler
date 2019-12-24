# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
# Если записать числа от 1 до 5 английскими словами (one, two, three, four, five), то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
# Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
# Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв, число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам британского английского.
#
# 21124

FIGURES = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
           8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
           16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: "nineteen"}
TENS = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}


def in_words(num):
    # thousands
    th = num // 1000
    if th != 0:
        resth = FIGURES[th] + 'thousand'
        num -= th * 1000
        # if num == 0 and th > 1:
        #     resth += 's'
    else:
        resth = ''
    # hundreds
    hu = num // 100
    if hu != 0:
        reshu = FIGURES[hu] + 'hundred'
        num -= hu * 100
        # if num == 0 and hu > 1:
        #     reshu += 's'
    else:
        reshu = ''
    # tens
    te = num // 10
    if te > 1:
        reste = ('and' if th+hu != 0 else '') + TENS[te]
        num -= te * 10
    elif num != 0:
        reste = 'and' if th+hu != 0 else ''
    else:
        reste = ''
    # rest
    if num != 0:
        resnum = FIGURES[num]
    else:
        resnum = ''
    return ''.join((resth, reshu, reste, resnum))


sum = 0
for value in range(1, 1001):
    sum += len(in_words(value))
print(sum)
