Alder = int(input("skriv inn alder"))

if Alder >= 21:
    print ("Du kan ta buss, bil og mopedsetvikat")
elif Alder >= 18:
    print ("Du kan ta bil og mopedsetvikat")
elif Alder >= 16:
    print ("Du kan ta mopedsetvikat")
else:
    print ("Du er ikkje gammel nokk til å ha eit setvikat")
