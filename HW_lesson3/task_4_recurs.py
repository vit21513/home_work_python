# 4.Напишите программу, которая будет
#  преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def num_to_bin(num):
    res = ''
    if num == 0:
        return
    else:
        res = res + str(num % 2)
        num_to_bin(num // 2)
        print(res, end='')


number = int(input("Введите число:"))

num_to_bin(number)
