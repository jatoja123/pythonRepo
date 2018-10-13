# To jest komentarz, tego kompjuter nie czyta

"""
   To jest string, ale mozna go uzyc 
   jako komentarz    
"""
#Podstawowe typy w Pythonie
#String 
owca = 'Ala ma kota'
owca1 = "Ala ma kota, kot ma Ale i koze krowe "
#Fajne operacje na napisach
owca[0] # wybierze pierwszy znak z napisu 
owca[0:4] # wyciaga znaki od indeksu 0 do indeksu 3
owca[3:7]
#print wyświetla w konsoli dana rzecz
print(owca[:7])
#sprwadzanie dlugosci napisu
len("napis")
#Liczby 
#Sa dwa typy liczbowe w pythonie int i float
owcaInt = -5
owcaFloat = 7.5
#Ciekawe zapisy
2**5 #32 -> 2 do 5
2e2 # 2* (10 do 2)
2e-2 # 2 * (10 do -2)
7%5 # zwraca reszte z dzielenia
# Boolean
prawda = True
falsz = False
##Uwaga roznice
# 1 + "7" zwaraca Error
str(1) + "7"
print(1,"7", owca )
#formatowanie napisow
print(f'Ala ma {17} kotow : {prawda}')