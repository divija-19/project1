#Task 4: List variables

#import the function keyword 
import keyword

#Define a function to get a program from the user 
def get_program():
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    program = []
    while True:
        line = input()
        if line.lower() == 'end':
            break
        program.append(line)
    return program

#define a function to print the program
def print_program(program):
    print("Program:")
    for line in program:
        print(line)

#define a function to list the variables
def list_variables(program):
    variables = set()
    python_keywords = set(keyword.kwlist)

    for line in program:
        words = line.split()
        for word in words:
            if word.isidentifier() and word not in python_keywords:
                if word[0].isalpha() and all(c.isalnum() or c == '_' for c in word):
                    variables.add(word)

#define a function to print the variables 
    print("Variables:")
    for var in sorted(variables):
        print(var)

#print the main menu
def main_menu(program):
    while True:
        print("=" * 34)
        print("Enter your choice:")
        print("1. Print program.")
        print("2. List.")
        print("0. Quit.")
        print("=" * 34)

        choice = input()

        if choice == '1':
            print_program(program)
        elif choice == '2':
            list_variables(program)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")
            
#define the main function 
def main():
    program = get_program()
    main_menu(program)

#run the main function
if __name__ == "__main__":
    main()