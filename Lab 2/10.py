import wikipedia
wikipedia.set_lang("pl")
tmp=wikipedia.page("Guido van Rossum")
a=tmp.content[0:100]
print(a.title())