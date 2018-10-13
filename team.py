osoby = ["Mariusz","Stojan","Abecadel","Pawel","Ktos"]
team1 = []
team2 = []
import random

try:
    for x in range(0,len(osoby)):
        team1.append(random.choice(osoby))
        team2.append(random.choice(osoby))

    print(osoby,team1,team2)
except ValueError as owcaError:
    print("blad")