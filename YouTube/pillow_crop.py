from PIL import Image

# img is now Pillow obj
img = Image.open("cat.png")
area = (100, 100, 200, 200)
cropped_img = img.crop(area)

# display in default image viewing program
img.show()

cropped_img.show()