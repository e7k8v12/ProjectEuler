#  https://projecteuler.net/problem=31
#  In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general
#  circulation:
#  1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#  It is possible to make £2 in the following way:
#  1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#  How many different ways can £2 be made using any number of coins?
#  https://euler.jakumo.org/problems/view/31.html
#  В Англии валютой являются фунты стерлингов £ и пенсы p, и в обращении есть восемь монет:
#  1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) и £2 (200p).
#  £2 возможно составить следующим образом:1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#  Сколькими разными способами можно составить £2, используя любое количество монет?
#
# 73682

import time

start_time = time.time()

search_value = 200

total = 0
for p1 in range(0, search_value + 1, 1):
    limit = search_value - (p1)
    for p2 in range(0, limit + 1, 2):
        limit = search_value - (p1 + p2)
        for p5 in range(0, limit + 1, 5):
            limit = search_value - (p1 + p2 + p5)
            for p10 in range(0, limit + 1, 10):
                limit = search_value - (p1 + p2 + p5 + p10)
                for p20 in range(0, limit + 1, 20):
                    limit = search_value - (p1 + p2 + p5 + p10 + p20)
                    for p50 in range(0, limit + 1, 50):
                        limit = search_value - (p1 + p2 + p5 + p10 + p20 + p50)
                        for p100 in range(0, limit + 1, 100):
                            limit = search_value - (p1 + p2 + p5 + p10 + p20 + p50 + p100)
                            for p200 in range(0, limit + 1, 200):
                                if p1 + p2 + p5 + p10 + p20 + p50 + p100 + p200 == search_value:
                                    total += 1
                                    # res1 = f'{total})\t'
                                    # res = []
                                    # if p200 != 0:
                                    #     res.append(f'{p200 // 200}x£2')
                                    # if p100 != 0:
                                    #     res.append(f'{p100 // 100}x£1')
                                    # if p50 != 0:
                                    #     res.append(f'{p50 // 50}x50p')
                                    # if p20 != 0:
                                    #     res.append(f'{p20 // 20}x20p')
                                    # if p10 != 0:
                                    #     res.append(f'{p10 // 10}x10p')
                                    # if p5 != 0:
                                    #     res.append(f'{p5 // 5}x5p')
                                    # if p2 != 0:
                                    #     res.append(f'{p2 // 2}x2p')
                                    # if p1 != 0:
                                    #     res.append(f'{p1}x1p')
                                    # print(res1, ' + '.join(res), f'= {search_value}')

print('\n', total)

end_time = time.time()

print('time:', end_time - start_time)
