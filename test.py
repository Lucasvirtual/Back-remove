from rembg import remove
from PIL import Image


input = Image.open("lucas.jpg")
output = remove(input)
output.save("lucas1.png")