#Task 3: Rabbytes' Extended Universe

#define a class called Rabbit which would be used to represent individual rabbits
class Rabbit:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.parents = []
        self.kittens = []

#define a class which would be used to manage the collection of rabbits  
class RabbitDatabase:
    def __init__(self):
        self.rabbits = []

#define a function to get or create rabbit 
    def get_or_create_rabbit(self, name):
        rabbit = next((r for r in self.rabbits if r.name == name), None)
        if not rabbit:
            rabbit = Rabbit(name)
            self.rabbits.append(rabbit)
        return rabbit

#define a function to create a rabbit
    def create_rabbit(self):
        while True:
            name = input("Input the new rabbit's name:\n")
            if not any(rabbit.name == name for rabbit in self.rabbits):
                self.rabbits.append(Rabbit(name))
                break
            else:
                #if the name is already in the database, print the following 
                print("That name is already in the database.")

#define a function to input the age of a rabbit 
    def input_age(self):
        while True:
            name = input("Input the rabbit's name:\n")
            rabbit = next((r for r in self.rabbits if r.name == name), None)
            if rabbit:
                age = int(input(f"Input {name}'s age:\n"))
                rabbit.age = age
                break
            else:
                #if the name is not in the database, print this 
                print("That name is not in the database.")

#define a function to list all the rabbits
    def list_rabbits(self):
        print("Rabbytes:")
        for rabbit in self.rabbits:
            age = rabbit.age if rabbit.age is not None else "Unknown"
            print(f"{rabbit.name} ({age})")

#define a function which would create parental relationship between rabbits
    def create_parental_relationship(self):
        parent_name = input("Input the parent's name:\n")
        kitten_name = input("Input the kitten's name:\n")
        
        parent = self.get_or_create_rabbit(parent_name)
        kitten = self.get_or_create_rabbit(kitten_name)
        
        parent.kittens.append(kitten)
        kitten.parents.append(parent)

#define a function to list the Family
    def list_direct_family(self):
        while True:
            name = input("Input the rabbit's name:\n")
            rabbit = next((r for r in self.rabbits if r.name == name), None)
            if rabbit:
                print(f"Parents of {rabbit.name}:")
                for parent in sorted(rabbit.parents, key=lambda x: x.name):
                    print(parent.name)
                print(f"Kittens of {rabbit.name}:")
                for kitten in sorted(rabbit.kittens, key=lambda x: x.name):
                    print(kitten.name)
                break
            else:
                #if the name is not in database then:
                print("That name is not in the database.")

#define a function to find the cousins of rabbit 
    def find_cousins(self):
        while True:
            name = input("Input the rabbit's name:\n")
            rabbit = next((r for r in self.rabbits if r.name == name), None)
            if rabbit:
                cousins = set()
                for parent in rabbit.parents:
                    for grandparent in parent.parents:
                        for uncle_aunt in grandparent.kittens:
                            if uncle_aunt != parent:
                                cousins.update(uncle_aunt.kittens)
                
                #Remove the rabbit itself from the cousins set
                cousins.discard(rabbit)
                
                print(f"Cousins of {rabbit.name}:")
                for cousin in sorted(cousins, key=lambda x: x.name):
                    print(cousin.name)
                break
            else:
                #if the name is not in database print this
                print("That name is not in the database.")

#define main function to run the program
def main():
    database = RabbitDatabase()

#print the main menu
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Create a Rabbit.")
        print("2. Input Age of a Rabbit.")
        print("3. List Rabbytes.")
        print("4. Create a Parental Relationship.")
        print("5. List Direct Family of a Rabbit.")
        print("6. Find Cousins of a Rabbit.")
        print("0. Quit.")
        print("==================================")

        choice = input()

        if choice == '1':
            database.create_rabbit()
        elif choice == '2':
            database.input_age()
        elif choice == '3':
            database.list_rabbits()
        elif choice == '4':
            database.create_parental_relationship()
        elif choice == '5':
            database.list_direct_family()
        elif choice == '6':
            database.find_cousins()
        elif choice == '0':
            break
        else:
            continue

#Run the main function if the code is executed directly
if __name__ == "__main__":
    main()