from PIL import Image

chris = Image.open("Chris.jpg")
cat = Image.open("cat.png")

# we are going to paste cat picture onto chris's picture
# need to make sure that the cat picture fits into chris

# cat 300 x 300

# the coordinate of chris picture where the cat picture will go
area = (100, 100, 400, 400)
chris.paste(cat, area)

chris.show()