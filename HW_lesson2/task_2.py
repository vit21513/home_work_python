# 2. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]


number = int(input("Введите  число N:  "))

def res_number_n(num):
    res= 1
    for i in range(num+1):
        print (num)
        res*=1

res_number_n(number)