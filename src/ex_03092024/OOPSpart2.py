class Person:
    def __init__(self):
        self.name = input("enter the name")
        self.age = input("Enter age")

    def display_person_inputs(self):
        print(self.name)
        print(self.age)

abject_calling = Person()
abject_calling.display_person_inputs()