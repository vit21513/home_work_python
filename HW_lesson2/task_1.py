# 1. Подсчитать сумму цифр в вещественном числе


def sum_num(num):
    res = 0
    for i in num:
        if i == '.' or i == ',':  # вслучае если пользователь введет в числе вместо точки запятую
            continue
        res += int(i)
    return res


number = input("Введите вещественное число:")

print(f' сумма чисел в числе {number} составляет {sum_num(number)}')
