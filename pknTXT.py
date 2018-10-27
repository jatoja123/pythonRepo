import random
from tkinter import *
twojepunkty = 0
punktyprze = 0
window = Tk()
window.title("Kamien Papier Nozyce")
window.geometry('800x600')

lbl = Label(window, text = "Wybierz cos!")
lbl.grid(row = 1, column = 0, padx=(0,20) )

lbl2 = Label(window, text = "")
lbl2.grid(row = 3,column = 0)

btnKam = Button(window, text = "Kamien")
btnKam.grid(column = 1,row = 2)
btnPap = Button(window, text = "Papier")
btnPap.grid(column = 2,row = 2)
btnNoz = Button(window, text = "Nozyce")
btnNoz.grid(column = 3,row = 2)

def kamienDef():
    przeciwnik = random.randint(1,3)
    if przeciwnik == 1:
        lbl2.configure(text = "przegrana!")
    elif przeciwnik == 2:
        lbl2.configure(text = "remis!")
    elif przeciwnik == 3:
        lbl2.configure(text = "wygrana!")
def papierDef():
    przeciwnik = random.randint(1,3)
    if przeciwnik == 1:
        lbl2.configure(text = "remis!")
    elif przeciwnik == 2:
        lbl2.configure(text = "wygrana!")
    elif przeciwnik == 3:
        lbl2.configure(text = "przegrana!")
def nozyceDef():
    przeciwnik = random.randint(1,3)
    if przeciwnik == 1:
        lbl2.configure(text = "wygrana!")
    elif przeciwnik == 2:
        lbl2.configure(text = "przegrana!")
    elif przeciwnik == 3:
        lbl2.configure(text = "remis!")


btnKam.configure(command = kamienDef)
btnPap.configure(command = papierDef)
btnNoz.configure(command = nozyceDef)




for x in range(0,3):
    przeciwnik = random.randint(1,3)
    twoj = input("co wybierasz? ")
    if twoj == "papier":
        if przeciwnik == 1:
            print("remis!")
        elif przeciwnik == 2:
            print("wygrales!")
            twojepunkty+=1
        elif przeciwnik == 3:
            print("przegrales!")
            punktyprze+=1
    elif twoj == "kamien":           
        if przeciwnik == 1:
            print("przegrales!")
            punktyprze+=1
        elif przeciwnik == 2:
            print("remis!")
        elif przeciwnik == 3:
            print("wygrales!")
            twojepunkty+=1
    elif twoj == "nozyce":
        if przeciwnik == 1:
            print("wygrales!")
            twojepunkty+=1
        elif przeciwnik == 2:
            print("przegrales!")
            punktyprze+=1
        elif przeciwnik == 3:
            print("remis!")
    else:
        print("wpisales cos zlego")

print("twoje punkty: ")
print(twojepunkty)
print("punkty przeciwnika: ")
print(punktyprze)
if twojepunkty > punktyprze:
    print("wygrales gre!")
elif twojepunkty == punktyprze:
    print("zremisowales gre!")
else:
    print("przegrales gre!")



window.mainloop()