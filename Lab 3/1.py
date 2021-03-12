from typing import Set
s: Set[int] = set() 

for i in range(0,10):
    a=input("Podaj wartosc z klawiatury: ")
    s.add(a)

print(s)
