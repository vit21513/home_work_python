# 2. Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.


num = int(input("Введите натуральное число N:"))


def simple_multipliers(number):
    multipliers = []
    mult = 2
    temp = number
    while mult * mult <= number:
        if number % mult == 0:
            multipliers.append(mult)
            number //= mult
        else:
            mult += 1
    multipliers.append(number)
    return multipliers


print(
    f'список простых множителей числа {num} составляет {simple_multipliers(num)}')
