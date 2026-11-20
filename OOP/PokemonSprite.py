
baseLocation = "C:\\Users\\oster\\OneDrive - Vestland fylkeskommune\\Documents\\Vg2\\IT2\\Main-repository-IT2\\OOP"
import climage
from PIL import Image
import Pokemon



background = Image.new("RGB", (800, 600), (0, 0, 0))


PlayerSprites = [baseLocation + "\\CharB.png", baseLocation + "\\Ven B.png", baseLocation + "\\Blast B.png"]
EnemySprites = [baseLocation + "\\ChaF.png", baseLocation + "\\VenF.png", baseLocation + "\\Blast F.png"]

"Pvalg og Evalg"
player = Image.open(PlayerSprites[0])
enemy = Image.open(EnemySprites[1])

player.thumbnail((250, 250))
enemy.thumbnail((400, 400)) 
player = player.resize((300, 300))
enemy = enemy.resize((250, 250))


background.paste(player, (50, 350))
background.paste(enemy, (500, 50))

background.save("pokemon_battle.png")

print(climage.convert("pokemon_battle.png", width=75))

"""
from tkinter import *
import tkinter as tk
from tkinter import PhotoImage


# Create the main window
window = Tk()

# Load the image 
image = PhotoImage(file ="pokemon_battle.png")

# Create a label to display the image
image_label = tk.Label(window, image=image)
image_label.pack()

window.mainloop()
"""