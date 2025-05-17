#Author: Elise Merrifield
#CIS129 Lab 12
#Codding a class to create and store pet information as an object

# Define the Pet class

class Pet:
    def __init__(self, name="", pet_type="", age=0):
        self.name = name
        self.pet_type = pet_type
        self.age = age
    #mutator methods
    def set_pet_name(self, name):
        if name.strip():
            self.name = name
        else:
            print("Error: Field must be filled in")
    def set_pet_type(self, pet_type):
        if pet_type.strip():
            self.pet_type = pet_type
        else:
            print("Error: Field must be filled in")
    def set_pet_age(self, age):
        if age.strip():
            self.age = age
        else:
            print("Error: Field must be filled in")

    #accessor methods
    def get_pet_name(self):
        return  self.name
    def get_pet_type(self):
        return self.pet_type
    def get_pet_age(self):
        return self.age

    #main module
def main():
        #create pet object
        animal = Pet()

        while True:
            input_pet_name = input("Enter pet name:")
            if input_pet_name.strip():
                animal.set_pet_name(input_pet_name)
                break

        while True:
            input_pet_type = input("Enter a pet type:")
            if input_pet_type.strip():
                animal.set_pet_type(input_pet_type)
                break

        while True:
            input_pet_age = input("Enter pet age.")
            if input_pet_age.isdigit():
                animal.set_pet_age(input_pet_age)
                break
            else:
                print("Invalid input. Please enter numeric age.")
        print("\nPet Details:")
        print("The pet name is:", animal.get_pet_name())
        print("The pet type is:", animal.get_pet_type())
        print("The pet age is:", animal.get_pet_age())



if __name__ == '__main__':
    main()