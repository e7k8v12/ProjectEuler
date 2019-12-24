# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# Дана следующая информация (однако, вы можете проверить ее самостоятельно):
# 1 января 1900 года - понедельник.
# В апреле, июне, сентябре и ноябре 30 дней.
# В феврале 28 дней, в високосный год - 29.
# В остальных месяцах по 31 дню.
# Високосный год - любой год, делящийся нацело на 4, однако последний год века (ХХ00) является високосным в том и только том случае, если делится на 400.
# Сколько воскресений выпадает на первое число месяца в двадцатом веке (с 1 января 1901 года до 31 декабря 2000 года)?
#
# 171

from datetime import datetime, timedelta

cur_date = datetime(1901, 1, 1)
end_date = datetime(2000, 12, 31)
num_of_sundays = 0
while cur_date <= end_date:
    if cur_date.day == 1 and cur_date.weekday() == 6:
        num_of_sundays += 1
    cur_date += timedelta(days=1)

print(num_of_sundays)
