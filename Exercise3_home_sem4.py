'''
Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.
'''
import random
list1=[]

for i in range(10):
    n = random.randint(0,10)
    list1.append(n)
print("      list1= ", list1)

list2=[]
list_result=[]
for i in range(len(list1)):
    flag=True
    list2.append(list1[i])
    for j in range(len(list2)-1):
        if list1[i]==list2[j]:
            if list1[i] in list_result:
               list_result.remove(list1[i])
            flag=False
    if flag==True:
       list_result.append(list1[i])
    else:
        flag=True
print("list_result= ", list_result)