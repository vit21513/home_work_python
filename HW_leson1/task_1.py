# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


def days(num):
    if num < 1 or num > 7:
        print("Вы ввели некоректное число")
    elif num >= 6:
        print("это выходной день")
    else:
        print("это рабочий день")


day = int(input("Введите день недели "))

days(day)
