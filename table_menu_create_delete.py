#Task 8: Table Creation and Deletion

#import the function csv
import csv
#import the tabulate function to print tables
from tabulate import tabulate

#define a function to read csv files
def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        return list(reader)

#define a function to list tables 
def list_tables(tables):
    table_info = []
    for i, table in enumerate(tables):
        if table:  # Only list non-None tables
            table_info.append([i, len(table[0]), len(table)])
    print(tabulate(table_info, headers=["Index", "Columns", "Rows"], tablefmt="simple"))

#define a function to display tables 
def display_table(tables):
    while True:
        index = int(input("Choose a table index (to display):\n"))
        if 0 <= index < len(tables) and tables[index]:
            print(tabulate(tables[index][1:], headers=tables[index][0], tablefmt="simple"))
            break
        else:
            #if the table index is incorrect, then print this 
            print("Incorrect table index. Try again.")

#define a function to duplicate a table 
def duplicate_table(tables):
    while True:
        index = int(input("Choose a table index (to duplicate):\n"))
        if 0 <= index < len(tables) and tables[index]:
            tables.append(tables[index].copy())
            break
        else:
            #if the table index is incorrect, then print this 
            print("Incorrect table index. Try again.")

#define a function to create a table
def create_table(tables):
    while True:
        index = int(input("Choose a table index (to create from):\n"))
        if 0 <= index < len(tables) and tables[index]:
            column_indices = input("Enter the comma-separated indices of the columns to keep:\n")
            column_indices = [int(i) for i in column_indices.split(',')]
            new_table = [[row[i] for i in column_indices] for row in tables[index]]
            tables.append(new_table)
            break
        else:
            #print this error message if the table index is incorrect
            print("Incorrect table index. Try again.")

#define a function to delete a table
def delete_table(tables):
    while True:
        index = int(input("Choose a table index (for table deletion):\n"))
        if 0 <= index < len(tables) and tables[index]:
            tables[index] = None
            break
        else:
            #print this error message if the table index is incorrect  
            print("Incorrect table index. Try again.")

#define the main menu
def main():
    tables = [
        read_csv('grades.csv'),
        read_csv('class_students.csv'),
        read_csv('rabbytes_club_students.csv'),
        read_csv('rabbytes_data.csv')
    ]

#print the main menu
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. List tables.")
        print("2. Display table.")
        print("3. Duplicate table.")
        print("4. Create table.")
        print("5. Delete table.")
        print("0. Quit.")
        print("==================================")
        
        choice = input()
        
        if choice == '1':
            list_tables(tables)
        elif choice == '2':
            display_table(tables)
        elif choice == '3':
            duplicate_table(tables)
        elif choice == '4':
            create_table(tables)
        elif choice == '5':
            delete_table(tables)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

#run the main menu
if __name__ == "__main__":
    main()