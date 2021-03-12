from typing import List

lista: List[List[int]] = [

]

for i in range(0,4):
    a=input(f"Podaj elementy {i+1} wiersza w nawiasach kwadratowych oddzielając przecinkami:\n")
    lista.append(a) 

for i in range(4):
    print(lista[i])
