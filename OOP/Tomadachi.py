sult = 5
energi = 5
glede = 5
sult2 = 5
energi2 = 5
glede2 = 5
inp = 1

namn1 = input(str("Kva skal den første tomodachien heite "))
namn2 = input(str("Kva skal den andre tomodachien heite "))

while inp != 0:
    print(f"""{namn1}: sult {sult}, energi {energi}, glede {glede}
{namn2}: sult {sult2}, energi {energi2}, glede {glede2}
Hvilket dyr vil du handle med 1: {namn1} 2: {namn2}""")
    valg = input()
    if valg == "1":
        sult2 =+ 1
        glede2 =-1
        print ("""kva handling vil du utføre:
               0 avslutt program, 1 mat, 2 leke, 3 sove""")
        inp = input()
        
        print (f"Du har drepte {namn1}")
        if  inp == "1":
            sult -=2
        elif inp == "2" and energi > 1:
            glede +=3
            energi -=2 
            sult +=1
        elif inp == "2":
            print (f"{namn1} har ikkje nokk energi til å leke")
        elif inp == "3":
            energi +=4, 
            sult +=1
        else: print("Skriv inn ein nummer asosiert med handlingen du vil utføre")

    if valg == "2":
        sult =+ 1
        glede =-1
        print ("""kva handling vil du utføre:
               0 avslutt program, 1 mat, 2 leke, 3 sove""")
        inp = input()
        
        print (f"Du har drepte {namn1}")
        if  inp == "1":
            sult2 -=2
        elif inp == "2" and energi > 1:
            glede2 +=3
            energi2 -=2
            sult +=1
        elif inp == "2":
            print (f"{namn1} har ikkje nokk energi til å leke")
        elif inp == "3":
            energi2 +=4, 
            sult +=1
        else:
            print("Skriv inn ein nummer asosiert med handlingen du vil utføre")   

    else: print("skriv it ett nummer assosiert med Tomodachien du vil handle med")


    

    