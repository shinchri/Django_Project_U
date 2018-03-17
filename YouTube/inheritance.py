class Parent():

    def print_last_name(self):
        print("Shin")


class Child(Parent):

    def print_first_name(self):
        print("chris")

    # ovveriding parent's classes method
    def print_last_name(self):
        print("Mo")


chris = Child()
paul = Parent()

chris.print_first_name()
chris.print_last_name()