osoby = ["Mariusz","Stojan","Abecadel","Pawel","Ktos","Pimpek","Bombek"]
team1 = []
team2 = []
import random

try:
    powt = int(len(osoby)/2)
    if powt < (len(osoby)/2):
        powt+=1
    
    for x in range(0,powt):
        ran = random.choice(osoby)
        team1.append(ran)
        osoby.remove(ran)
        if len(osoby) > 0:
            ran = random.choice(osoby)
            team2.append(ran)
            osoby.remove(ran)
    print(osoby,team1,team2)
except ValueError as owcaError:
    print("blad")