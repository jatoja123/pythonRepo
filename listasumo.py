lista = []
wynik = 0
dlugosc = input("wpisz dlugosc listy: ")

for x in range(0,int(dlugosc)):
    lista.append(input("wpisz element listy: "))

i = 0
for x in range(0,int(dlugosc)):
    if int(lista[i]) > -1:
        wynik += int(lista[i])
    i+=1
print(wynik)