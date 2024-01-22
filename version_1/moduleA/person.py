from moduleB.pet import Pet


class Person():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.pet = None

    def print_person_data(self):
        print(f"This person is called {self.name} and it's {self.age} years old.")
        if self.pet:
            print(f"This person has a pet!: {self.pet.print_pet_info()}")

    def change_age(self, new_age):
        self.age = new_age

    def change_name(self, newName):
        self.name = newName

    def set_Pet(self, pet: Pet):
        self.pet = pet
