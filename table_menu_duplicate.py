#Task 7: Table Duplication

#import the function csv
import csv
#Import the tabulate function to print tables
from tabulate import tabulate

#define a function to read csv files  
def read_csv(filename):
    with open(filename, 'r') as file:
        return list(csv.reader(file))

#define a function to list tables 
def list_tables(tables):
    table_info = [["Index", "Columns", "Rows"]]
    for i, table in enumerate(tables):
        table_info.append([i, len(table[0]), len(table)])
    print(tabulate(table_info, headers="firstrow", tablefmt="simple"))

#define a function to display a table 
def display_table(tables):
    while True:
        index = int(input("Choose a table index (to display):\n"))
        if 0 <= index < len(tables):
            print(tabulate(tables[index], headers="firstrow", tablefmt="simple"))
            break
        else:
            #if the table index is incorrect, print this
            print("Incorrect table index. Try again.")

#define a function to duplicate a table
def duplicate_table(tables):
    while True:
        index = int(input("Choose a table index (to duplicate):\n"))
        if 0 <= index < len(tables):
            tables.append(tables[index].copy())
            break
        else:
            #if the table index is incorrect, print this
            print("Incorrect table index. Try again.")

#define the main menu
def main():
    tables = [
        read_csv("grades.csv"),
        read_csv("class_students.csv"),
        read_csv("rabbytes_club_students.csv"),
        read_csv("rabbytes_data.csv")
    ]

#print the main menu 
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. List tables.")
        print("2. Display table.")
        print("3. Duplicate table.")
        print("0. Quit.")
        print("==================================")

        choice = input()

        if choice == "1":
            list_tables(tables)
        elif choice == "2":
            display_table(tables)
        elif choice == "3":
            duplicate_table(tables)
        elif choice == "0":
            break

#run the main menu
if __name__ == "__main__":
    main()