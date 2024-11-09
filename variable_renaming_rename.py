#Task 6: Renaming variables

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

#define a function to print the program
def print_program(program):
    print("Program:")
    for line in program:
        print(line)

#define a function to list the variables
def list_variables(program):
    variables = get_variables(program)
    print("Variables:")
    for var in sorted(variables):
        print(var)
    return variables

#define a function to get the variables
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

#define a function to format the variables
def format_variable(program, variables):
    while True:
        var_name = input("Pick a variable:\n")
        if var_name in variables:
            new_name = to_snake_case(var_name)
            for i, line in enumerate(program):
                program[i] = re.sub(r'\b' + var_name + r'\b', new_name, line)
            break
        else:
            #if the variable name is invalid then print this
            print("This is not a variable name.")
    return program

#define a function to rename the variable 
def rename_variable(program, variables):
    while True:
        var_name = input("Pick a variable:\n")
        if var_name in variables:
            while True:
                new_name = input("Pick a new variable name:\n")
                if new_name not in variables:
                    for i, line in enumerate(program):
                        program[i] = re.sub(r'\b' + var_name + r'\b', new_name, line)
                    variables.remove(var_name)
                    variables.add(new_name)
                    break
                else:
                    #if the variable name is already present then print this
                    print("This is already a variable name.")
            break
        else:
            print("This is not a variable name.")
    return program, variables

#print the main menu
def main_menu(program):
    variables = get_variables(program)
    while True:
        print("=" * 34)
        print("Enter your choice:")
        print("1. Print program.")
        print("2. List.")
        print("3. Format.")
        print("4. Rename.")
        print("0. Quit.")
        print("=" * 34)

        choice = input()

        if choice == '1':
            print_program(program)
        elif choice == '2':
            list_variables(program)
        elif choice == '3':
            program = format_variable(program, variables)
            variables = get_variables(program)
        elif choice == '4':
            program, variables = rename_variable(program, variables)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

#define the main menu
def main():
    program = get_program()
    main_menu(program)

#run the main menu
if __name__ == "__main__":
    main()