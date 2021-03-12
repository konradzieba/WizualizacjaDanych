from typing import Dict  

di: Dict[str, str] = {
    'gotować': 'cook',
    'robić': 'do',
    'tworzyć': 'make',
    'pływać': 'swim',
    'grać': 'play',
    'pić': 'drink',
    'woda': 'water',
    'trawa': 'grass',
    'piwo': 'beer',
}

while 1:
    a=str(input("Podaj polskie słowo:\n"))
    if a=='end':
        break
    if a in di:
        print("Tłumaczenie słowa {a} - {di[a]}")
    else:
        print("Twoje słowo nie znajduje się w słowniku, podaj jego tłumaczenie:\n")
        b=str(input())
        di[a] = b
for element in di:
    print(element,"-",di[element])