sult = 5
energi = 5
glede = 5

namn = input("Kva skal tomodachien heite? ")

inp = 1

while inp != 0:
    inp = int(input(f"""
{namn}: sult {sult}, energi {energi}, glede {glede}
1: Mate  2: Leke  3: Sove  0: Avslutt
Velg: """))

    if inp == 0:
        print(f"Du har drept {namn}")
    elif inp == 1:
        sult -= 3
        glede += 1
    elif inp == 2 and energi > 1:
        glede += 3
        energi -= 2
        sult += 1
    elif inp == 2:
        print(f"{namn} har ikkje nok energi til å leike")
    elif inp == 3:
        energi += 4
        sult += 1
    else:
        print("Skriv inn eit nummer som høyrer til handlinga.")