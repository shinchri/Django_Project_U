from PIL import Image
#
from PIL import ImageFilter

# cat, duck = RGBA
# 518(dog) = RGB

dog = Image.open("518.jpg")

# to change format (RGB default)
# L = black and white
#black_white = dog.convert("L")


blur = dog.filter(ImageFilter.BLUR)
detail = dog.filter(ImageFilter.DETAIL)
edges = dog.filter(ImageFilter.FIND_EDGES)

#blur.show()
dog.show()
detail.show()
#edges.show()