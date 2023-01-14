'''
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
'''
import random
list1=[]

for i in range(10):
    n = random.randint(0,10)
    list1.append(n)
print("list1= ", list1)

list2=[]
for x in list1:
    for y in list2:
        if x==y:
            list2.remove(y)
    list2+=[x]
print("list2= ", list2)
