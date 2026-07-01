import csv
import os
FILE_NAME = 'expenses.csv'

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Description', 'Amount'])

def add_expense(date, description, amount):
     with open(FILE_NAME, 'a', newline='') as file:
         writer = csv.writer(file)
         writer.writerow([date, description, amount])
     print("Expense added successfully!")

def view_expenses():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def total_expenses():
    total = 0
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        next(reader) 
        for row in reader:
            total += float(row[2])
    print("Total expenses=", total)
          
date = input("Enter the date (DD-MM-YYYY): ")
description = input("Enter expense description: ")
amount = input("Enter amount: ")
add_expense(date, description, amount)
view_expenses()
total_expenses()