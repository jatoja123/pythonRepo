
f = open("doPisanie.txt","w+")

linijki = int(input("Ile linijek? : "))

for x in range(linijki):
    tekst = input("napisz linijke: ")+"\n"
    f.write(tekst)