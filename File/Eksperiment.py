#Integer = heiltal Float = desimaltall
# {bruk disse koloene for integers og floats når du begynner å printe ein string}
# ctrl + * disabler kode
#stor bosktav imitere konstanter
# // er dividerer og runder av til nærmeste tall. % gir rest av devisjonen. Deling gjør integrs om til floats

# omkrets formel sirkel= 2r*pi . Areal formel sirkel= på*r**2
#import math as m
#radius = 42
#omkrets = 2 * radius * m.pi
#areal = m.pi * radius**2
#print (f"Omkretsen av sikerlen er {omkrets} areal av sirkelen er {areal}") 
#print ("Omkretsen av sikerlen er", omkrets, "areal av sirkelen er ", areal) 
 
#sitat = "Datamaskiner er ubrukelige. De kan bare gi oss svar."
#print("Sitatets lengde:", len(sitat)) 
#print("Tegnene til og med indeks 11:", 
#print("Tegnene fra og med indeks 28:", 
#print("Tegnene med indeks 16 til 25:", 
# - teller bakover 

#tall = int(input("skriv eit tall for å sjekke om det er posetivt eller negativt "))
#if tall == 67:
    #print("OMGFG DREP DEG SJØLV DU FORTJENNER OIKKJEUVF Å LRVEE HENG DEG SJØVKVNEUGFHFHHFH")
#elif tall > 0:
    #print ("Talle dit er posetivt")
#elif tall < 0:
    #print ("Talle dit er negativt")
#else:
    #print ("Talle dit er null, altså ikkje posetivt eller negativt")

import random


DScore = 0
PScore = 0

#Potensial oppgradering, gjør om til += 1, sjer om til arrey

while PScore < 3 and DScore < 3:

    DataValg = str(random.choice (["stein", "saks", "papir", "øgla", "spock"]))
    PlayerValg = str(input("skriv inn stein, saks, papir, øgla eller spock:  ")).lower() 
    print (f"Datamaskin valgte: {DataValg}")

    if PlayerValg not in ("stein", "saks", "papir", "øgla", "spock"):
        print ("Du skreiv ikkje inn stein, saks, papir, øgla eller spock ")
    elif DataValg == PlayerValg:
        print(f"Du og datamaskin begge valgte {DataValg}.Du har {PScore} poeng. Datamaskin har {DScore} poeng ")
    elif (PlayerValg == "stein" and DataValg == "øgla" or DataValg == "saks") or (PlayerValg == "saks" and DataValg == "papir" or DataValg == "øgla") or (PlayerValg == "pappir" and DataValg == "stein" or DataValg == "spock") or (PlayerValg == "øgla" and DataValg == "spock" or DataValg == "pappir") or (PlayerValg == "spock" and DataValg == "saks" or DataValg == "stein"):
        PScore = PScore + 1
        print (f"Du fikk eit poeng. Du har {PScore} poeng. Datamaskin har {DScore} poeng")
    else:
        DScore = DScore + 1 
        print (f" Datamaskin fikk poeng. Du har {PScore} poeng. Datamaskin har {DScore} poeng")

if PScore == 3:
    print ("Du vant")
else: 
    print ("Du tapte")

#Noko feil med kalkulasjon p papir slår d saks
