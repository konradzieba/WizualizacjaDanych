from typing import List, Any
li: List[Any] = []
blokada=bool(0)
while blokada==0:
    a=input("Podaj wartosc, która chcesz dodac: ")
    if a in li:
        blokada=1
    else:
        li.append(a)