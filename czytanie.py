from tkinter import *

window = Tk()
window.title("Czytanie Pliku")
window.geometry('800x600')

lbl = Label(window, text = "")
lbl.grid(row = 1, column = 0, padx=(0,20) )

f = open("doZad.txt")
f1 = f.readlines()
i = 0

for x in f1:
    lbl = Label(window, text = x)
    lbl.grid(row = i, column = 0, padx=(0,20) )
    i+=1

window.mainloop()
