# manual_csv_operations_fixed.py
import os

FILENAME = "employees.csv"

# Create file with sample data if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        f.write("ID,Name,Department,Salary\n")
        f.write("1,John Doe,IT,50000\n")
        f.write("2,Jane Smith,HR,55000\n")
        f.write("3,Bob Johnson,Finance,60000\n")
        f.write("4,Alice Brown,IT,52000\n")
    print(f"{FILENAME} created with sample data.")

# (a) Read CSV and display as formatted table
def read_csv():
    with open(FILENAME, "r") as f:
        lines = f.readlines()
    data = [line.strip().split(",") for line in lines]
    
    print("\nEmployee Data:")
    for row in data:
        print("{:<5} {:<15} {:<10} {:<10}".format(*row))
    return data

# (b) Add a new row
def add_row(new_row):
    with open(FILENAME, "a") as f:
        f.write(",".join(new_row) + "\n")
    print("\nRow added successfully!")

# (c) Update a specific cell (e.g., salary for ID=2)
def update_cell(emp_id, column_name, new_value):
    data = read_csv()
    headers = data[0]
    col_index = headers.index(column_name)
    
    for i in range(1, len(data)):
        if data[i][0] == emp_id:
            data[i][col_index] = new_value
            break
    
    with open(FILENAME, "w") as f:
        for row in data:
            f.write(",".join(row) + "\n")
    print(f"\nUpdated {column_name} for employee ID={emp_id}")

# (d) Delete a row by condition (e.g., Department='IT')
def delete_row_by_condition(column_name, value):
    data = read_csv()
    headers = data[0]
    col_index = headers.index(column_name)
    
    data = [row for row in data if row[col_index] != value]
    
    with open(FILENAME, "w") as f:
        for row in data:
            f.write(",".join(row) + "\n")
    print(f"\nDeleted rows where {column_name}='{value}'")

# (e) Sort by a specific column (e.g., Salary)
def sort_by_column(column_name):
    data = read_csv()
    headers = data[0]
    col_index = headers.index(column_name)
    
    sorted_data = [headers] + sorted(data[1:], key=lambda x: int(x[col_index]))
    
    print(f"\nData sorted by {column_name}:")
    for row in sorted_data:
        print("{:<5} {:<15} {:<10} {:<10}".format(*row))

# --- Demo of operations ---
if __name__ == "__main__":
    read_csv()
    add_row(["5", "Charlie Lee", "Marketing", "48000"])
    update_cell("2", "Salary", "58000")
    delete_row_by_condition("Department", "IT")
    sort_by_column("Salary")