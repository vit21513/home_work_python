
#Задача с семминара
#  ' дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул'
# Необходимо получить словарь, в котором ключи – слова, значения – количество слов в строке:
# {'дом': 2, 'окно': 2, 'дверь': 2, 'стена': 1, 'кухня': 1, 'стол': 2, 'стул': 3}


stroka= 'дом, окно, дверь, стена, кухня, стол, стул, дверь, дом, стул, стол, окно, стул'
slovar= dict()
spisok=stroka.split(", ")
multi= set(spisok)


for i in  multi:
    index= spisok.count(i)
    slovar[i]=index

print(slovar)    


# вариант с  dict complication

sorted_list = {k:spisok.count(k) for k in multi}  

print(sorted_list)