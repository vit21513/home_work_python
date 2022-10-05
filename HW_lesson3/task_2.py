# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем
# первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*

import math
def first_end_ellem(array):

    index = len(array)-1
    result = []
    res = 1
    #index = index//2
    print(index)
    inde=math.ceil(index/2)
    for i in range(inde):
        res = array[i]*array[(i+1)*-1]
        result.append(res)
    return result


spisok = [2, 3, 4, 5, 6]  # 12 15 16
spisok2 = [2, 3, 5, 6]   # 12 15
spisok3 = [2, 3, 5, 6, 2, 3]     # 6 6 30
spisok4 = [2, 3, 5, 6, 2, 3, 5, 2]   # 4 15 15 12


print(first_end_ellem(spisok))
