# Задача №33: Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



import random


def creaty_file(st):
    with open('file_result.txt', 'w') as data:
        data.write(st)

    

def create_str(k):


    koff_sp=[]
    for i in range(k+1):
        koff_sp.append(random.randint(0,101))
    res = ''
    if len(koff_sp) <= 1:
        res = 'x = 0'
    else:
        for i in range(len(koff_sp)):
            if i != len(koff_sp) - 1 and koff_sp[i] != 0 and i != len(koff_sp) - 2:
                res += f'{koff_sp[i]}x^{len(koff_sp)-i-1}'
                if koff_sp[i+1] != 0:
                    res += '+'
            elif i == len(koff_sp) - 2 and koff_sp[i] != 0:
                res += f'{koff_sp[i]}x'
                if koff_sp[i+1] != 0:
                    res += '+'
            elif i == len(koff_sp) - 1 and koff_sp[i] != 0:
                res += f'{koff_sp[i]} =0'
            elif i == len(koff_sp) - 1 and koff_sp[i] == 0:
                res += '= 0'
    return res

k = int(input("Введите натуральную степень k = "))

creaty_file(create_str(k))
