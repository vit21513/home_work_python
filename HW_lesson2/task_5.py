# 5. Реализовать алгоритм перемешивания списка.

import random

spisok = []

for i in range(0, 21):
    spisok.append(random.randint(1, 100))


def sort(array):
    res = []
    res2 = []
    for i in array:
        if i % 2 == 0:
            res.append(i)
        else:
            res2.append(i)
    res2.sort()
    res.sort()
    res.extend(res2)
    return res


print(f' список до сортировки {spisok}')

print(f' список после сортировки {sort(spisok)}')
