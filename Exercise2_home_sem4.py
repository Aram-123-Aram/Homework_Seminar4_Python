'''
Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.
'''
n = int(input("Enter the number n= "))
list=[]
i=2
while n/i >=1:
    while n %i ==0:
        list+=[i]
        n=n/i
    i+=1
print(" -> ", list)