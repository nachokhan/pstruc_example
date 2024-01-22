class Pet:

    def __init__(self, pet_name: str, pet_age: int):
        self.name = pet_name
        self.age = pet_age

    def print_pet_info(self):
        print(f"This pet's name is {self.name} and it is {self.age} years old.")

    def change_pet_age(self, new_age):
        self.age = new_age

    def change_pet_name(self, new_name):
        self.name = new_name
