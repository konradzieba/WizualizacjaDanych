import math
A=int(input("Podaj parametr A: "))
B=int(input("Podaj parametr B: "))
C=int(input("Podaj parametr C: "))



delta = (B*B) - (4*A*C)
print("Delta: ", delta)
minus_b = int(B*(-1))
if delta==0:
    x0 = minus_b/(2*A)
    print("Jedno miejsce zerowe: ", x0)
elif delta >0:
    x1 = (minus_b-math.sqrt(delta))/(2*A)
    x2 = (minus_b+math.sqrt(delta))/(2*A)
    print("Dwa miejsca zerowe: " ,round(x1,2) ,"i" ,round(x2,2))
else:
    print("Brak rozwiazan - delta < 0")
