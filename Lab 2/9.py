import wikipedia
wikipedia.set_lang("pl")
a=wikipedia.summary("Olsztyn")
print(a.upper())