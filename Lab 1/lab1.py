import os
import wikipedia
from faker import Faker
wikipedia.set_lang("pl")
#print(wikipedia.summary("Python"))
#print(wikipedia.page("Mauritius").url)
print(wikipedia.page("Galapagos").content)
#print(os.getcwd())
#print(os.getpid())
#os.mkdir("test")
#os.mkdir("test")
"""
print(Faker().name()) #imie
print(Faker().address()) #adres
print(Faker().text()) #tekst

for i in range(3):
    print(Faker().name())
    print(Faker().address())
"""
