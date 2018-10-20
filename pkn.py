import random
twojepunkty = 0
punktyprze = 0
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