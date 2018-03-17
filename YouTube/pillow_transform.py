from PIL import Image

# dog image = (278, 350)
dog = Image.open("518.jpg")
square_dog = dog.resize((250, 250))

flip_dog = dog.transpose(Image.FLIP_LEFT_RIGHT)
spin_dog = dog.transpose(Image.ROTATE_90)

dog.show()
square_dog.show()

flip_dog.show()