"Add type system, more moves, trainer, (try including parant), real batteling mechanics(switch), crit,"

import random as r
"Kaspar sugestion(annan fil)"
fire = {
    "fire": 0.5,
    "water": 0.5,
    "grass": 2,
    "ice": 2
}
water = {
    "water": 0.5,
    "grass":0.5,
    "fire": 2,
    "ground":2
}
grass = {
    "grass": 0.5,
    "fire": 0.5,
    "water": 2,
    "ground":2
}
ice = {
    "fire": 0.5,
    "water":0.5,
    "grass": 2,
    "flying": 2,
    "ground": 2
}
ground = {
    "flying": 0,
    "grass": 0.5,
    "fire": 2,
    "electric": 2,
    "poison": 2
}
electric = {
    "ground":0,
    "grass":0.5,
    "flying":2,
    "water":2
}
flying = {
    "electric":0.5,
    "grass":2,
}

class Move:
    def __init__(self, name, power, Atype, type:dict, Rtype):
        self.name = name
        self.power = power
        self.Atype = Atype
        self.type = type
        self.Rtype = Rtype

ice_shard = Move("Ice shard",20,"Physical",ice,"ice")
earthquake =Move("Eartquake",35,"Physical",ground, "ground")
fireball =Move("Fireball", 20, "Special", fire, "fire")
lightning =Move ("Lightning",25,"Special", electric, "electric")

"fire placeholder menhar ikkje noko å sei."

class Status(Move):
    def __init__(self, name, power, Atype, type, Rtype, effect):
        super().__init__(name, power, Atype, type, Rtype)
        self.effect = effect
    

iron_deffense =Status("iron defense", "+2 defense", "Status", "Selfstatus", "fire",[1, 1, 2, 1, 1, 1])         



class Pokemon:
    def __init__(self, name, level, bhp, batk, bdf, bspatk, bspdf, bsp, type1, type2):
        self.name = name
        self.level = level
        self.bhp = bhp
        self.batk = batk
        self.bspatk = bspatk
        self.bdf = bdf
        self.bspdf = bspdf
        self.bsp = bsp
        self.type1 = type1
        self.type2 = type2

  
    def statcalc(self, x):
        return (2*x*self.level)/100 +5

    def stats(self):
        self.hp = (2 * self.bhp * self.level)/100 + self.level + 10
        self.atk = self.statcalc (self.batk) 
        self.spatk = self.statcalc(self.bspatk)
        self.df = self.statcalc(self.bdf + 8)
        self.spdf = self.statcalc(self.bspdf + 8)
        self.sp = self.statcalc(self.bsp)
        return self.hp, self.atk, self.spatk, self.df, self.spdf, self.sp

    
    def is_alive(self):
        return self.hp > 0

    
    def Pvelg_move(self):
        self.move = [ice_shard, earthquake, fireball, lightning, iron_deffense]
        (f"Velg eit move {self.move}")
        for i in range(len(self.move)):
            print(f"{i + 1}. {self.move[i].name.capitalize()}")
            print(f"Power: {self.move[i].power}")
        valg = int(input("Skriv inn nummeret på angrepet du vil bruke: ")) - 1
        while valg != valg<0 and valg>4:
            valg = int(input("Svaret ditt var ikkje gyldig. Skriv inn nummeret på angrepet du vil bruke: ")) - 1
        Avalg = self.move[valg]
        return Avalg

    def Evelg_move(self):      
        self.move = [ice_shard, earthquake, fireball, lightning, iron_deffense]        
        Avalg = self.move[r.randint(0,3)]
        return Avalg 
Charizard = Pokemon("Charizard", 50, 78, 84, 78, 109, 85, 100, "fire","flying")
Venusaur = Pokemon("Venusaur", 50, 80, 82, 83, 100, 100, 80,"grass", "poison")
Blastoise = Pokemon("Blastoise", 50, 79, 83, 100, 85, 105, 78, "water", 1)

Lpokemon = [Charizard, Venusaur, Blastoise]
(f"Velg ein pokemon {[Lpokemon]}")
for i in range(len(Lpokemon)):
    print(f"{i + 1}. {Lpokemon[i].name.capitalize()}")
Pvalg = int(input("Skriv inn nummeret på pokemonen du vil bruke: ")) - 1  
while Pvalg > 2 and Pvalg < 0:
    Pvalg = int(input("Svaret ditt var ikkje gyldig. Skriv inn nummeret på pokemonen du vil bruke: ")) - 1  
ppokemon = Lpokemon[Pvalg]
epokemon = Lpokemon[r.randint(0,2)]



"""add crit, replace is alive"""
def Match(x,y):
    x.stats()
    y.stats()
    
    Php = x.hp
    Patk = x.atk
    Pdf = x.df 
    Pspatk = x.spatk
    Pspdf = x.spdf
    Psp = x.sp
    Pstats=[Php, Patk, Pdf, Pspatk, Pspdf, Psp]
    Ehp = y.hp
    Eatk = y.atk
    Edf = y.df
    Espatk = y.spatk
    Espdf = y.spdf
    Esp = y.sp
    Estats=[Ehp, Eatk, Edf, Espatk, Espdf, Esp]
    

    print(f"{x.name} has {x.hp} hp")
    print(f"{y.name} has {y.hp} hp")

    def Pattack (x,b,y,z):
        Pdamage = ((2*x.level/100+2)*z.power* b / y)* r.randint(85,100)/100
        return Pdamage
    def Sattack (x,b,y,z):
        Sdamage = ((2*x.level/100+2)*z.power* b / y)* r.randint(85,100)/100
        return Sdamage

    
        

    while Php > 0 and Ehp > 0:
        PStab = 1
        EStab = 1
        Tie_breaker = 0
        if Esp == Psp:
            Tie_breaker= r.randint(0,1)
        Pmove = x.Pvelg_move()
        Emove =y.Evelg_move()
       
        Ptype = Pmove.type
        Etype = Emove.type
        PEffectivness1 = 1
        PEffectivness2 = 1
        EEffectivness1 = 1
        EEffectivness2 = 1

        if Ptype != "Selfstatus":
            for i in Ptype.keys():
                if i == y.type1:
                    PEffectivness1 = Ptype[y.type1]
                    print(f"player first {PEffectivness1}")              
                if i == y.type2:
                    PEffectivness2 = Ptype[y.type2]
                    print(f"player first {PEffectivness1}")

        PEffectivness = PEffectivness1 * PEffectivness2
        print(f"player effectivness: {PEffectivness}")

        if Etype != "Selfstatus":
            for i in Etype.keys():
                if i == x.type1:
                    EEffectivness1 = Etype[x.type1]
                    print(f"Enemy first {EEffectivness1}") 
                if i == x.type2:
                    EEffectivness2 = Etype[x.type2]
                    print(f"Enemy second {EEffectivness2}")

        EEffectivness = EEffectivness1 * EEffectivness2
        print(f"Enemy effectivness: {EEffectivness}")

        if Pmove.Rtype == x.type1 or Pmove.Rtype == x.type2:
            PStab = 1.5
    
        if Emove.Rtype == y.type1 or Emove.Rtype == y.type2:
            EStab = 1.5


        if Psp > Esp or Tie_breaker == 1: 
            print (f"{x.name} used {Pmove.name}") 
            if Pmove.Atype == "Physical":
                Dmglost= round(Pattack(x,Patk,Edf,Pmove) * PStab * PEffectivness)
                Ehp-=Dmglost
                print(f"{y.name} lost {Dmglost} hp")
                if Ehp >= 0:
                    print (f"{y.name} has {Ehp}hp")
                else:
                    print (f"{y.name} has 0hp")
            elif Pmove.Atype == "Special":
                Dmglost = round(Sattack(x,Pspatk,Espdf,Pmove) * PStab * PEffectivness)
                Ehp= Ehp-Dmglost
                print(f"{y.name} lost {Dmglost} hp")
                if Ehp >= 0:
                    print (f"{y.name} has {Ehp}hp")
                else:
                    print (f"{y.name} has 0hp")
            else: 
                if Pmove.type == "Selfstatus":
                    print(Php, Patk, Pdf, Pspatk, Pspdf, Psp)
                    for i in range(len(Pstats)):
                        Pstats[i] = Pstats[i] * Pmove.effect[i]
                        print(Pstats) 
                    print(Php, Patk, Pdf, Pspatk, Pspdf, Psp)

                else:
                    print(Estats)
                    for i in range(len(Estats)):
                        Estats[i] = Estats[i] * Pmove.effect[i]
                    print(Estats)

            if Ehp > 0:
                
                print (f"{y.name} used {Emove.name}")
                if Emove.Atype == "Physical":
                    Dmglost = round(Pattack(y,Eatk,Pdf,Emove) * EStab * EEffectivness)
                    Php -= Dmglost
                    print(f"{x.name} lost {Dmglost} hp")
                    if Php >= 0:
                        print (f"{x.name} has {Php}hp")
                    else:
                        print (f"{x.name} has 0hp")
                elif Emove.Atype == "Special":
                    Dmglost = round(Sattack(y,Espatk,Pspdf,Emove) * EStab * EEffectivness)
                    Php= Php-Dmglost
                    print(f"{x.name} lost {Dmglost} hp")
                    if Php >= 0:
                        print (f"{x.name} has {Php}hp")
                    else:
                        print (f"{x.name} has 0hp")
                else:
                 if Emove.type == "Selfstatus":
                    print(Estats)
                    for i in range(len(Estats)):
                        Estats[i] = Estats[i] * Emove.effect[i]                        
                        print(Estats)
                    else:
                        print(Pstats)
                        for i in range(len(Pstats)):
                            Pstats[i] = Pstats[i] * Emove.effect[i]
                        print(Pstats)                           
        else:
            print (f"{y.name} used {Emove.name}")
            if Emove.Atype == "Physical":
                Dmglost = round(Pattack(y,Eatk,Pdf,Emove) * EStab * EEffectivness)
                Php= Php-Dmglost
                print(f"{x.name} lost {Dmglost} hp")
                if Php >= 0:
                    print (f"{x.name} has {Php}hp")
                else:
                    print (f"{x.name} has 0hp")
                
            elif Emove.Atype == "Special": 
                Dmglost = round(Sattack(y,Espatk,Pspdf,Emove) * EStab * EEffectivness)
                Php= Php-Dmglost
                print(f"{x.name} lost {Dmglost} hp")
                if Php >= 0:
                    print (f"{x.name} has {Php}hp")
                else:
                    print (f"{x.name} has 0hp") 
            else:    
                if Emove.type == "Selfstatus":
                    print(Estats)
                    for i in range(len(Estats)):
                        Estats[i] = Estats[i] * Emove.effect[i]                        
                    print(Estats)
                else:
                    print(Pstats)
                    for i in range(len(Pstats)):
                        Pstats[i] = Pstats[i] * Emove.effect[i]
                    print(Pstats)               
              
            if Php > 0:
                print (f"{x.name} used {Pmove.name}")
                if Pmove.Atype == "Physical":
                    Dmglost= round(Pattack((x,Patk,Edf,Pmove)) * PStab * PEffectivness)
                    Ehp= Ehp-Dmglost
                    print(f"{y.name} lost {Dmglost} hp")
                    if Ehp >= 0:
                        print (f"{y.name} has {Ehp}hp")
                    else:
                        print (f"{y.name} has 0hp")

                elif Pmove.Atype == "Special":
                    Dmglost = round(Sattack(x,Pspatk,Espdf,Pmove) * PStab * PEffectivness)
                    Ehp= Ehp-Dmglost
                    print(f"{y.name} lost {Dmglost} hp")
                    if Ehp >= 0:
                        print (f"{y.name} has {Ehp}hp")
                    else:
                        print (f"{y.name} has 0hp")
                else:
                    if Pmove.type == "Selfstatus":
                        print(Pstats)
                        for i in range(len(Pstats)):
                            Pstats[i] = Pstats[i] * Pmove.effect[i]                        
                        print(Pstats)
                    else:
                        print(Estats)
                        for i in range(len(Pstats)):
                            Estats[i] = Estats[i] * Pmove.effect[i]
                        print(Estats)
        
        if Php <= 0:
            print("you lost")
            break

        if Ehp <=0:
            print("you won")
            break

Match(ppokemon, epokemon)
