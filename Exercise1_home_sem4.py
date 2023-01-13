'''
Вычислить число c заданной точностью d
Пример:
- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
'''
import math
print(f"pi= {math.pi}")
d = float(input("Enter the d= "))
count=0
while d!=1:
    count+=1
    d=10*d
result=round(math.pi,count)
print(f" -> pi= {result}")
