# 4.Напишите программу, которая будет
#  преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def num_to_bin(nem):
    res = ''
    if nem == 0:
        return
    else:
        res = res+str(nem % 2)
        num_to_bin(nem//2)
        print(res, end='')
    return


number = int(input("Введите число:"))

num_to_bin(number)
