from tkinter import *

window = Tk()
#zmienia tytul okna
window.title("Nasa Hacker")
#zmienia wielkosc okna
window.geometry('800x600')
#element ktory ma text albo obrazek
lbl = Label(window, text = "Podaj kod do systemu nasa!")
lbl.grid(row = 1, column = 0, padx=(0,20) )

lbl2 = Label(window, text = "Podaj nazwe uzytkownika!")
lbl2.grid(row = 0,column = 0, padx=(0,20))
#pole txtowe
pTekstowe = Entry(window)
pTekstowe.grid(row=0,column=1)

pTekstowe2 = Entry(window)
pTekstowe2.grid(row=1,column=1)
#przycisk
btn = Button(window, text = "Kliknij by zhackowac nasa...")
btn.grid(column = 1,row = 2)

def hackingNasa():
    #text = pTekstowe.get()
    #lbl.configure(text = "ZHACKOWANO NASA. Podlaczono do bazy danych...")
    #pTekstowe.delete(0,END)
    lbl3 = Label(window, text = "uzytkownik: " + pTekstowe.get() )
    lbl3.grid(row = 3, column = 0, padx=(0,20) )
    lbl4 = Label(window, text = "kod dostepu: "+pTekstowe2.get() )
    lbl4.grid(row = 4, column = 0, padx=(0,20) )
    lbl5 = Label(window, text = "Zhackowano NASA... Uzyskano dostep do bazy danych NASA..." )
    lbl5.grid(row = 5, column = 1, padx=(0,20) )

btn.configure(command = hackingNasa)

window.mainloop()