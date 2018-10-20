listaLenght = input("Ile elementow w liscie? ")
lista = []
try:
    listaLenght = int(listaLenght)
    for x in range(0,listaLenght):
        element = input("jaki element? ")
        lista.append(element)

    listaWynik = int(lista[0])
    del lista[0]
    for x in range(1,listaLenght): 
        listai = lista[0]  
        del lista[0] 
        listaWynik = listaWynik * int(listai)
    print(listaWynik)
except ValueError as owcaError:
    print("nie wpisales liczby")