'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''
'''
#variant1
k = int(input("Enter the number: k= "))
list=[]
n1,n2=1,-1
for i in range(k-2):
    i=n1-n2
    list+=[i]
    n1=n2
    n2=i
for x in reversed(list):
    print(x, end=" ")
print(-1,1,end=" ")
n1,n2=0,1
print(n1,n2,end=" ")
for i in range(2,k+1):
    i=n1+n2
    print(i, end=" ")
    n1=n2
    n2=i
'''
#variant2    [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
k = int(input("Enter the number: k= "))

list=[1, 0, 1]
list1=[]
for i in range(k-1):
    list1+=[list[1]+list[2]]
    list[1]=list[2]
    list[2]=list1[i]

list=[1, 0, 1]
list2=[]
for i in range(k-1):
    list2+=[list[1]-list[0]]
    list[1]=list[0]
    list[0]=list2[i]

list=[1, 0, 1]
list2.reverse()
list2.extend(list)
list2.extend(list1)
print(f"k={k}  ->  Fibonachi numbers= {list2}")
