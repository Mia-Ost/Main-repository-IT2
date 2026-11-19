# print("Hei".upper())

# print([1, 2, 3].pop())

# i = 1
# print(type(i))

"""Balatro"""

class Handtype:
    def __init__(self, planet, bchip, bmult, ichip, imult):
        self.planet = planet
        self.bchip = bchip
        self.bmult = bmult
        self.ichip = ichip
        self.imult = imult

    def level(self, x):
        return f"{(self.bchip + (x-1) * self.ichip)} * {(self.bmult + (x-1) *self.imult)} = {(self.bchip + (x-1) * self.ichip) * (self.bmult + (x-1) *self.imult)}"

Highcard = Handtype("Pluto",5,1,10,1)
pair = Handtype("Mercury",10,2,15,1)
two_pair = Handtype("Uranus",20,2,20,1) 
three_of_a_kind = Handtype("Venus",30,3,20,2)
straight = Handtype("saturn",30,4,30,3)
flush = Handtype("Jupiter",35,4,15,2)
full_house = Handtype("Earth",40,4,25,2)
four_of_a_kind = Handtype("Mars",60,7,30,3)
straight_flush = Handtype("Neptune",100,8,40,4)
royal_flush = Handtype("Neptune",100,8,40,2)
five_of_a_kind = Handtype("Planet X",120,12,35,3)
flush_house = Handtype("Ceres",140,14,40,4)
flush_five = Handtype("Eris",160,16,50,3)


print(four_of_a_kind.level(1))

"""
from rich_pixels import Pixels
from rich.console import Console

console = Console()
pixels = Pixels.from_image_path("as.jpg")
console.print(pixels) """

