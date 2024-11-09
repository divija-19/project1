#Task 1: Rabbytes' Age

#define a class called Rabbit 
class Rabbit:
    def __init__(self, name):
        self.name = name
        self.age = None

#define a class called RabitDatabase
class RabbitDatabase:
    def __init__(self):
        self.rabbits = []

#define a function to create a rabbit 
    def create_rabbit(self):
        while True:
            name = input("Input the new rabbit's name:\n")
            if not any(rabbit.name == name for rabbit in self.rabbits):
                self.rabbits.append(Rabbit(name))
                break
            else:
                print("That name is already in the database.")

#Way to input the age of an existing rabbit
    def input_age(self):
        while True:
            name = input("Input the rabbit's name:\n")
            rabbit = next((r for r in self.rabbits if r.name == name), None)
            if rabbit:
                age = int(input(f"Input {name}'s age:\n"))
                rabbit.age = age
                break
            else:
                print("That name is not in the database.")

#Way to list all rabbits present in the database
    def list_rabbits(self):
        print("Rabbytes:")
        for rabbit in self.rabbits:
            if rabbit.age is not None:
                print(f"{rabbit.name} ({rabbit.age})")
            else:
                print(f"{rabbit.name} (Unknown)")

#Print the main menu
def main():
    database = RabbitDatabase()
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Create a Rabbit.")
        print("2. Input Age of a Rabbit.")
        print("3. List Rabbytes.")
        print("0. Quit.")
        print("==================================")
        my_choice = input()
        if my_choice == "1":
            database.create_rabbit()
        elif my_choice == "2":
            database.input_age()
        elif my_choice == "3":
            database.list_rabbits()
        elif my_choice == "0":
            break

#Run the main function if the code is executed directly
if __name__ == "__main__":
    main()