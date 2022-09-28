# 2. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]


number = int(input("Введите  число N:  "))  


def res_number_n(num):
    res = 1
    multi = []
    for i in range(1, num+1):
        res *= i
        multi.append(res)
    return multi


print(res_number_n(number))
