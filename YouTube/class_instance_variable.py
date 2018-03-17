class Girl:

    # class variable
    gender = "Female"

    def __init__(self, name):
        # instance variable
        self.name = name

girl1 = Girl("Lindsey")
girl2 = Girl("Rachel")

print(girl1.gender)
print(girl2.gender)
print(girl1.name)
print(girl2.name)