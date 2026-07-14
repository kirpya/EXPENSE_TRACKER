# ==========================================
# IMPORTS
# ==========================================
import csv
import os
from datetime import datetime

# ==========================================
# GLOBAL VARIABLES
# ==========================================

expenses = []
budget = None
currency = None
emergency = 0

FILE_NAME = "expense.csv"

# ==========================================
# FILE HANDLING FUNCTIONS
# ==========================================

def create_file():

    """
    Create the CSV file and write the header
    if the file does not already exist.
    """

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,"w",newline = "") as file:
             writer = csv.writer(file)
            
             writer.writerow([
                 "Date" ,
                 "Category"  ,
                 "Amount" ,
                 "Description" ,
             ])


def save_expense(expense):

    """
    Save a single expense to the CSV file.
    """

    with open(FILE_NAME,"a",newline="") as file:
        writer=csv.writer(file)

        writer.writerow([
                 expense["date"]  ,
                 expense["category"]  ,
                 expense["amount"] ,
                 expense["description"] ,
             ])

def save_all_expenses():
    """
    Save all expenses from the expenses list
    to the CSV file.
    """

    with open (FILE_NAME,"w",newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Date",
            "Category",
            "Amount",
            "Description",
        ])

        for expense in expenses:
            writer.writerow([
                expense["date"],
                expense["category"],
                expense["amount"],
                expense["description"]
            ])


def load_expenses():

    """
    Load all expenses from the CSV file
    into the expenses list.
    """

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME,"r") as file:

            reader = csv.DictReader(file)

            for row in reader:

                expenses.append({
                    "date" : row["Date"],
                    "category" : row["Category"],
                    "amount" :float(row["Amount"]),
                    "description" : row["Description"],
                })

# ==========================================
# BUDGET FUNCTIONS
# ==========================================


def set_budget():
    """
    Allow the user to choose a currency and
    set the total budget amount.
    """
## Ask to choose currency:
    print("\nAvailable Currency")

    print("-" * 30)

    print("1. INR (₹)")
    print("2. USD ($)")
    print("3. GBP (£)")
    print("4. EUR (€)")
    
#enter currency
    currency = input("Enter your Currency:").strip().lower()
   
 #conditional statements to choose currency model      
    if currency == "inr"or currency =="1":
       currency ="₹"
       print("You choose INR (Indian Rupee) ")

    elif currency == "usd"or currency =="2" :
       currency = "$"
       print("You choose US Dollar")
    elif currency == "gbp"or currency =="3":
        currency = "£"
        print("You choose British Pounds")
    elif currency == "eur" or currency =="4":
        currency = "€"
        print("You choose Euro")
    else:
         print("Please enter currency :")
         return None,None
    
    #Enter Budget
    try:
        budget_amount = float(input("Enter your Budget Amount:"))
        print(f"Your Budget is {currency} {budget_amount}")
        return budget_amount , currency
    except ValueError:
        print("Please enter a valid amount.")
        return None,None

    

    
def emergency_fund(currency):
    """
    Allow the user to create an emergency fund
    and return the selected amount.
    """


    #Ask user to create an emergency fund
    
    user_choice = input("Do you want to create an emergency fund? (Y/N): ").strip().lower()

    if user_choice in ("yes","y"):
            
            print("You Choose YES")
            try:
                 set_limit=float(input("Enter the extending limit you want :"))
                 print(f"Emergency fund set to:{currency}{set_limit}")
                 return set_limit
            except ValueError:
                print("Enter a valid Amount:")
                return None
           

    elif  user_choice in ("no","n"):
            print("You Choose NO")
            return 0

    else:
            print("Enter yes or no")

            return None

    
# ==========================================
# EXPENSE FUNCTIONS
# ==========================================


def add_expense():
    """
    Collect expense details from the user,
    save them to the expenses list,
    and store them in the CSV file.
    """

    date = datetime.now().strftime("%Y-%m-%d")
 
    while True:
      
      category =input("Enter the expense category:").strip().title()
      
      

      if not category:
          print("Enter category:")
          continue


      try:
       amount = float(input(f"Enter the expense amount you want to add :{currency}"))
      except ValueError:
          print("Error ! Enter a valid number")
          continue
      
     
      
      description=input("Enter a description :")
      description = description.strip().title()
      if not description:
          print("Enter description:")
          continue
    

      if amount <= 0:
        print("Amount must be greater than zero")
        continue
      
      expense = {
          "category": category,
          "amount": amount,
          "description": description,
          "date" : date ,
      }
      expenses.append(expense)

      save_expense(expense)

      print ("Expense added successfully ")
      break

def display_single_expense(expense):
    """
    Display the details of a single expense
    in a readable format.
    """
    print(f"Category    : {expense['category']}")
    print(f"Amount      : {currency}{expense['amount']}")
    print(f"Description : {expense['description']}")
    print(f"Date        : {expense['date']}")
    print("*" * 30)
    
# ==========================================
# ANALYSIS FUNCTIONS
# ==========================================
    
def view_expenses():
    """
    Display all saved expenses.
    """
    
    if not expenses:
        print("No Expense Found")
    else:
        for expense in expenses:
            display_single_expense(expense)
    


def search_expenses():
    """
    Search expenses by category,
    date, or description.
    """
    while True:
        print("\nSearch Expenses")
        print("1. Search by Category")
        print("2. Search by Date")
        print("3. Search by Description")
        print("4. Back")
        
    
        search_choice = input ("Enter your Choice : ").strip()

        if search_choice == "1" :
          search_value = input("Enter category:").strip().title()
          found = False
          for expense in expenses:
              if search_value == expense['category']:
                  found = True
                  display_single_expense(expense)
                  
          if not found:    
           print("No Matching Expense Found.")
           
                
              
                  
        elif search_choice == "2":
            search_value = input("Enter Date (YYYY-MM-DD) :").strip()
            found = False

            for expense in expenses:
                if search_value == expense["date"]:
                    found = True
                    display_single_expense(expense)
                    
            if not found:
               print("Invalid choice")
               


        elif search_choice == "3":
            search_value = input("Enter Description:").strip().title()
            found = False
            for expense in expenses:
                if search_value == expense['description']:
                    found = True
                    display_single_expense(expense)
                    
            if not found:
               print("Invalid choice")
               

        elif search_choice == "4" :
         break
        else:
          print("Invalid Choice! Please try again.")

def delete_expense():
    """
    Delete a selected expense
    from the expenses list.
    """
    if not expenses:
        print("Invalid Choice")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        display_single_expense(expense)

    try:  
        choice = int(input("Enter the expense number to delete: "))
        index = choice - 1
        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(index)

            save_all_expenses()

            print("Expense deleted successfully")
            display_single_expense(deleted)
        else:
            print("Invalid Number")
    except ValueError:
        print("Please Enter a Valid number.")


    
def update_expenses():
    """
    Update the category, amount,
    or description of an existing expense.
    """
    if not expenses:
        print("No expenses found.")
        return
    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        display_single_expense(expense)
    
    try:
        number= int(input("\nEnter expense number to update:"))
        index = number - 1
        if 0<= index < len(expenses):
            expense = expenses[index]

            while True:
                print("\nUpdate Expense")
                print("1. Update Category")
                print("2. Update Amount")
                print("3. Update Description")
                print("4. Back")

                update_choice = input("Enter your choice:").strip().lower()

                if update_choice in ("category","1"):
                   new_category=input("Enter your New Category:").strip().title()
                   expense["category"]= new_category
                   save_all_expenses()
                   print("Category updated successfully.")
                elif update_choice in ("amount","2"):
                    new_amount =float(input(f"Enter your new Amount:({currency})"))
                    
                    if new_amount > 0:
                      expense["amount"] = new_amount

                    else:
                      print("Amount must be greater than zero.")
                    
                    save_all_expenses()
                    
                    print(f"Amount updated successfully to {currency}{new_amount}")


                elif update_choice in ("description","3"):
                    new_description = input("Enter your new description:").strip().title()
                    expense["description"] = new_description
                    save_all_expenses()
                    print("Description updated successfully.")
                elif update_choice in ("back","4"):
                    break
                else:
                    print("No Expense found")
            print("\nUpdated Expense:")
            display_single_expense(expense)

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")

def calculate_total():
    """
    Calculate and return the total amount
    of all expenses.
    """

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total



def calculate_total_expense():
    """
    Calculate and display the total
    amount spent on all expenses.
    """

    if not expenses:
       print("No expenses found.")
       return
    
    total = calculate_total()

    print(f"Total expense: {currency}{total}")
    



def remaining_budget():
    """
    Calculate and display the
    remaining budget after expenses.
    """


    if budget is None:
        print("set your budget first")
        return
    
    total= calculate_total()
    remaining=budget - total
    print(f"Remaining Budget : {currency}{remaining}")
    if remaining<0:
        print("Warning ! you have exceed your budget")



def summary():

    """
    Display budget, total expenses,
    emergency fund and remaining budget.
    """

    if budget is None:
        print("Please set your budget first.")
        return

    total = calculate_total()

    remaining = budget - total

    print("\n===== Expense Summary =====")
    print(f"Budget            : {currency}{budget}")
    print(f"Total Expenses    : {currency}{total}")
    print(f"Emergency Fund    : {currency}{emergency}")
    print(f"Remaining Budget  : {currency}{remaining}")
    

# ==========================================
# MAIN PROGRAM
# ==========================================


def main():
    """
    Display the main menu and
    control the flow of the program.
    """
    global budget , currency, emergency 

    while True:
        print("\n===== Expense Tracker Menu =====")
        print("1. Set Budget")
        print("2. Emergency Fund")
        print("3. Add Expense")
        print("4. View Expenses")
        print("5. Search Expenses")
        print("6. Delete Expense")
        print("7. Update Expense")
        print("8. Total Expense")
        print("9. Remaining Budget")
        print("10.Summary")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")

        try:
            choice = int(choice)

            if choice == 1:
                budget , currency = set_budget()

            elif choice == 2:
                if currency is None:
                    print("Please set your budget first:")
                else :
                 emergency = emergency_fund(currency)

            elif choice == 3:
                if budget is None:
                    print("Please set your budget first:")
                else :
                 add_expense()

            elif choice == 4:
                if budget is None:
                    print("Please set your budget first:")
                    print("Add your Expenses first:")
                else:
                  view_expenses()

            elif choice == 5:
                search_expenses()

            elif choice == 6:
                delete_expense()

            elif choice == 7:
                update_expenses()

            elif choice == 8:
                calculate_total_expense()

            elif choice == 9:
                remaining_budget()

            elif choice == 10:
                summary()

            elif choice == 11:
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 11.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    create_file()
    load_expenses()
    main()
