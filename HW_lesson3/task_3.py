# 3.Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


array = [1.1, 1.2, 3.1, 5, 10.01]
array2 =[2.3,2,1,4,3,4,0,5]
array3 =[2.3,2,1,4,3.9,4,0,5]


def max_min_float(spisok):

    temp_spisok = []
    for i in spisok:
        if type(i) != float:
            continue
        temp = i-int(i)
        temp_spisok.append(temp)
    temp_spisok.sort()
    if len(temp_spisok)==1:                 # если в исходном списке только одно вещественное число
        result= temp_spisok[0]
    else:
        result = temp_spisok[len(temp_spisok)-1]-temp_spisok[0]
    return round(result,2)                    #округлил так как иногда кучу нулей после запятой выводит   


print(f'Разница между минимальным и максимальным значением составляет {max_min_float(array)}')


 

