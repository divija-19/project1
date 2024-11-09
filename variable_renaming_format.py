#Task 5: Formatting variables

#import the functions keyword and re
import keyword
import re

#define a function to get a program from the user
def get_program():
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    program = []
    while True:
        line = input()
        if line.lower() == 'end':
            break
        program.append(line)
    return program

#define a function to print program
def print_program(program):
    print("Program:")
    for line in program:
        print(line)

#define a function to list variables 
def list_variables(program):
    variables = get_variables(program)
    print("Variables:")
    for var in sorted(variables):
        print(var)
    return variables

#define a function to get variables
def get_variables(program):
    variables = set()
    python_keywords = set(keyword.kwlist)

    for line in program:
        words = line.split()
        for word in words:
            if word.isidentifier() and word not in python_keywords:
                if word[0].isalpha() and all(c.isalnum() or c == '_' for c in word):
                    variables.add(word)
    return variables

#define a function which would change normal font to snake case
def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

#define a function to format a variable 
def format_variable(program, variables):
    while True:
        var_name = input("Pick a variable:\n")
        if var_name in variables:
            new_name = to_snake_case(var_name)
            for i, line in enumerate(program):
                program[i] = re.sub(r'\b' + var_name + r'\b', new_name, line)
            break
        else:
            #if the typed variable is invalid then print this
            print("This is not a variable name.")
    return program

#print the main menu
def main_menu(program):
    while True:
        print("=" * 34)
        print("Enter your choice:")
        print("1. Print program.")
        print("2. List.")
        print("3. Format.")
        print("0. Quit.")
        print("=" * 34)

        choice = input()

        if choice == '1':
            print_program(program)
        elif choice == '2':
            variables = list_variables(program)
        elif choice == '3':
            variables = get_variables(program)
            program = format_variable(program, variables)
        elif choice == '0':
            break
        else:
            #if the choice is none of the following then print this
            print("Invalid choice. Please try again.")

#define the main menu
def main():
    program = get_program()
    main_menu(program)

#run the main menu
if __name__ == "__main__":
    main()