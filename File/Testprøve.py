"""
def dobbel_partall(liste):
    resultat = []
    for tall in liste:
        if tall % 2 == 0:
            resultat.append(tall * 2)
        else:
            resultat.append(tall)
    return resultat

tallene = [1, 2, 3, 4]
nye = dobbel_partall(tallene)
print(nye)
print(tallene)
print(sum(nye) > 10)
"""

""" Alder = int(input("Kor gammel er du?"))
StudenB = str(input("Har du student bevis")).lower()
if Alder < 0 or Alder > 120:
    print("Ugyldig alder")
elif Alder < 12:
    print("Ein billet koster 80kr")
elif Alder >= 67:
    print ("Ein billet koster 100kr")
elif Alder > 12 and Alder < 31 and StudenB == "ja":
    print("Ein billet koster 110kr")
else:
    print ("Ein billet koster 150") """

temperaturer = [4.5, -2.0, 1.5, -6.5, 0.0, 3.0, -1.5, 7.0, 5.5, -3.5]
print(temperaturer[-1], len(temperaturer))
print (sum(temperaturer))
for i in range temperaturer:
    


    
