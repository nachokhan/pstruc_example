from moduleB.pet import Pet


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.pet = None

    def print_person_data(self):
        print(f"This person is called {self.name} and is {self.age} years old.")
        if self.pet:
            self.pet.print_pet_info()  # Calling print_pet_info of Pet class

    def change_age(self, new_age):
        self.age = new_age

    def change_name(self, new_name):
        self.name = new_name

    def set_pet(self, pet: Pet):
        self.pet = pet
