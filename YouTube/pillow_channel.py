from PIL import Image

duck = Image.open("duck.png")

dog = Image.open("518.jpg")

# return tupple
r1, g1, b1 = dog.split()
r2, g2, b2 = duck.split()

# in any combination
new_img = Image.merge('RGB', (r1, g2, b1))