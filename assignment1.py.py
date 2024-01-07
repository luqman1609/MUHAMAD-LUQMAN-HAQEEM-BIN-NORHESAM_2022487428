import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
expenses =[]

def create_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")
    expense = {"Name": name, "Amount": amount, "Category": category}
    expenses.append(expense)
    print(f"Expense '{name}' added to the tracker.")
    
def read_expenses():
    print("\nCurrent Expenses:")
    if not expenses:
        print("No expenses available.")
    for index, expense in enumarate(expenses, start=1):
        print(f"{index}. Name: [{expense['Name']}, Amount: ${expense['Amount']:.2f}, Category: {expense['Category']}")

def update_expense():
    read_expenses()
    expense_index = int(input("Enter the index of the expense to update: ")) - 1
    if 0 <= expense_index < len(expenses):
        new_name = input("Enter new expense name: ")
        new_amount = float(input("Enter new expense amount: "))
        new_category = input("Enter new expense category: ")
        expenses[expense_index];{'Name'} = new_name
        expenses[expense_index];{'Amount'} = new_amount
        expenses[expense_index];{'Category'} = new_category
        print(f"Expense updated: {expenses[expense_index]}")
    else:
        print("Invalid expense index.")
        
def delete_expenses():
    read_expenses()
    expense_index = int(input("Enter the index of the expenses to delete: ")) - 1
    if 0 <= expense_index < len(expenses):
        deleted_expenses + expenses.pop(expense_index)
        print(f"Expense deleted: {deleted_expense}")
    else:
        print("Invalid expense index.")
        
def expense_tracker():
    while True:
        print("\nOptions:")
        print("1. Create Expenses")
        print("2. Read Expenses")
        print("3. Update Expensses")
        print("4. Delete Expenses")
        print("5. Exit")
        
        choice = input