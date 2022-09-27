# Задать список из n чисел последовательности  (1 + 1/n)^n и 
# вывести на экран их сумму.

number = int(input("Введите  число n:  "))

def list_numbers(num):
    res=[]
    for n in range(1,num+1):
        form= (1+ 1/n)**n
        res.append(form)
    return res    

    
print(list_numbers(number)) 

    

    
    