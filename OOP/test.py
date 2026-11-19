"""
from rich_pixels import Pixels
from rich.console import Console

console = Console()
pixels = Pixels.from_image_path("as.jpg")
console.print(pixels)
"""
import climage

# converts the image to print in terminal
# inform of ANSI Escape codes
output = climage.convert('ChaF.png')

# prints output on console.
print(output)