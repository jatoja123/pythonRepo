osoby = ["Mariusz","Stojan","Abecadel","Pawel","Ktos"]
team1 = []
team2 = []
import random

try:
    for x in range(0,len(osoby)):
        ran = random.choice(osoby)
        team1.append(ran)
        osoby.remove(ran)
        ran = random.choice(osoby)
        team2.append(ran)
        osoby.remove(ran)
    print(osoby,team1,team2)
except ValueError as owcaError:
    print("blad")