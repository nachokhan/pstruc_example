from moduleA.person import Person
from moduleB.pet import Pet


if __name__ == "__main__":

    juancito = Person("Juancito", 67)
    juancito_pet = Pet("Rocky", 10)

    mayra = Person("Mayra", 20)
    mayra_pet = Pet("Cuchuflo", 4)

    juancito.print_person_data()
    mayra.print_person_data()
