import csv
from tabulate import tabulate
import copy

def read_csv_files():
    # List of CSV files to read
    files = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']
    tables = []
    for file in files:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            tables.append(list(reader))  # Append each table as a list of rows
    return tables

def list_tables(tables):
    table_info = []
    for i, table in enumerate(tables):
        if table:  # Only include non-None tables
            table_info.append([i, len(table[0]), len(table)])  # Collect index, column count, and row count
    print(tabulate(table_info, headers=["Index", "Columns", "Rows"], tablefmt="simple"))  # Display table info

def display_table(tables):
    while True:
        # Prompt user to choose a table index
        index = int(input("Choose a table index (to display):\n"))
        if 0 <= index < len(tables) and tables[index]:
            # Display the chosen table with headers
            print(tabulate(tables[index][1:], headers=tables[index][0], tablefmt="simple"))
            break
        else:
            print("Incorrect table index. Try again.")  # Error message for invalid index

def duplicate_table(tables):
    while True:
        # Prompt user to choose a table index to duplicate
        index = int(input("Choose a table index (to duplicate):\n"))
        if 0 <= index < len(tables) and tables[index]:
            # Find the next available index to store the duplicated table
            new_index = next(i for i, table in enumerate(tables + [None]) if table is None)
            tables.append(copy.deepcopy(tables[index]))  # Append a deep copy of the selected table
            break
        else:
            print("Incorrect table index. Try again.")  # Error message for invalid index

def create_table(tables):
    while True:
        # Prompt user to choose a table index to create a new table from
        index = int(input("Choose a table index (to create from):\n"))
        if 0 <= index < len(tables) and tables[index]:
            # Prompt user to enter column indices to keep
            column_indices = input("Enter the comma-separated indices of the columns to keep:\n")
            column_indices = [int(i) for i in column_indices.split(',')]
            if all(0 <= i < len(tables[index][0]) for i in column_indices):
                # Create a new table with only the specified columns
                new_table = [[row[i] for i in column_indices] for row in tables[index]]
                # Find the next available index to store the new table
                new_index = next(i for i, table in enumerate(tables + [None]) if table is None)
                tables.append(new_table)  # Append the new table
                break
            else:
                print("Invalid column indices. Try again.")  # Error message for invalid indices
        else:
            print("Incorrect table index. Try again.")  # Error message for invalid index

def delete_table(tables):
    while True:
        # Prompt user to choose a table index to delete
        index = int(input("Choose a table index (for table deletion):\n"))
        if 0 <= index < len(tables) and tables[index]:
            tables[index] = None  # Mark the table as None to indicate deletion
            break
        else:
            print("Incorrect table index. Try again.")  # Error message for invalid index

def delete_column(tables):
    while True:
        # Prompt user to choose a table index from which to delete a column
        index = int(input("Choose a table index (for column deletion):\n"))
        if 0 <= index < len(tables) and tables[index]:
            # Prompt user to enter the index of the column to delete
            col_index = int(input("Enter the index of the column to delete:\n"))
            if 0 <= col_index < len(tables[index][0]):
                for row in tables[index]:
                    del row[col_index]  # Delete the specified column from each row
                break
            else:
                print("Invalid column index. Try again.")  # Error message for invalid column index
        else:
            print("Incorrect table index. Try again.")  # Error message for invalid index

def restore_table(tables):
    while True:
        # Prompt user to choose a table index to restore
        index = int(input("Choose a table index (for restoration):\n"))
        if 0 <= index < len(tables) and tables[index] is None:
            # List of files to restore from
            files = ['grades.csv', 'class_students.csv', 'rabbytes_club_students.csv', 'rabbytes_data.csv']
            if index < len(files):
                with open(files[index], 'r') as f:
                    reader = csv.reader(f)
                    tables[index] = list(reader)  # Restore the table from the corresponding file
            break
        else:
            print("Incorrect table index. Try again.")  # Error message for invalid index

def main_menu():
    # Read initial tables from CSV files
    tables = read_csv_files()
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. List tables.")
        print("2. Display table.")
        print("3. Duplicate table.")
        print("4. Create table.")
        print("5. Delete table.")
        print("6. Delete column.")
        print("7. Restore table.")
        print("0. Quit.")
        print("==================================")
        choice = input()
        
        if choice == '1':
            list_tables(tables)  # List all tables
        elif choice == '2':
            display_table(tables)  # Display a chosen table
        elif choice == '3':
            duplicate_table(tables)  # Duplicate a chosen table
        elif choice == '4':
            create_table(tables)  # Create a new table with selected columns
        elif choice == '5':
            delete_table(tables)  # Delete a chosen table
        elif choice == '6':
            delete_column(tables)  # Delete a column from a chosen table
        elif choice == '7':
            restore_table(tables)  # Restore a deleted table
        elif choice == '0':
            break  # Exit the menu

if __name__ == "__main__":
    main_menu()
