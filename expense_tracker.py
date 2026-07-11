from datetime import datetime

expenses=[]
budget = None
currency = None
emergency = 0

def set_budget():
## Ask to choose currency:
    print("1.INR")
    print("2.USD")
    print("3.GBP")
    print("4.EUR")
    
#enter currency
    currency = input("Enter your Currency:").strip().lower()
   
 #conditional statements to choose currency model      
    if currency == "inr"or currency=="1":
       currency ="₹"
       print("You choose INR (Indian Rupee) ")

    elif currency == "usd"or currency=="2" :
       currency = "$"
       print("You choose US Dollar")
    elif currency == "gbp"or currency=="3":
        currency = "£"
        print("You choose British Pounds")
    elif currency == "eur" or currency=="4":
        currency = "€"
        print("You choose Euro")
    else:
         print("Please enter currency :")
         return None,None
    
    #Enter Budget
    try:
        money = float(input("Enter your Budget Amount:"))
        print(f"Your Budget is {currency} {money}")
        return money , currency
    except ValueError:
        print("Please enter a valid amount.")
        return None,None

    

    
def emergency_fund(currency):


    #Ask user to create an emergency fund
    
        answer = input("Do you want to create an emergency fund? (Y/N): ").strip().lower()

        if answer in ("yes","y"):
            
            print("You Choose YES")
            try:
                 set_limit=float(input("Enter the extending limit you want :"))
                 print(f"Emergency fund set to:{currency}{set_limit}")
                 return set_limit
            except ValueError:
                print("Enter a valid Amount:")
                return None
           

        elif  answer in ("no","n"):
            print("You Choose NO")
            return 0

        else:
            print("Enter yes or no")

            return None

    



def add_expense():

    date = datetime.now().strftime("%Y-%m-%d")
 
    while True:
      
      category =input("Enter the expense category:")
      category=category.title()
      

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

      print ("Expense added successfully ")
      break

def display_expense(expense):
        print(f"Category    : {expense['category']}")
        print(f"Amount      : {currency}{expense['amount']}")
        print(f"Description : {expense['description']}")
        print(f"Date        : {expense['date']}")
        print("*" * 30)
    

    
          


    


def view_expenses():
    
    if not expenses:
        print("Invalid choice")
    else:
        for expense in expenses:
            display_expense(expense)
    


def search_expenses():
    while True:
        print("\nSearch Expenses")
        print("1. Search by Category")
        print("2. Search by Date")
        print("3. Search by Description")
        print("4. Back")
        
    
        select = input ("Enter your Choice : ").strip()

        if select == "1" :
          search = input("Enter category:").strip().title()
          found = False
          for expense in expenses:
              if search == expense['category']:
                  found = True
                  display_expense(expense)
                  
          if not found:    
           print("Invalid choice")
           
                
              
                  
        elif select == "2":
            search = input("Enter Date (YYYY-MM-DD) :").strip()
            found = False

            for expense in expenses:
                if search == expense["date"]:
                    found = True
                    display_expense(expense)
                    
            if not found:
               print("Invalid choice")
               


        elif select == "3":
            search = input("Enter Description:").strip().title()
            found = False
            for expense in expenses:
                if search == expense['description']:
                    found = True
                    display_expense(expense)
                    
            if not found:
               print("Invalid choice")
               

        elif select == "4" :
         break
        else:
          print("Invalid Choice! Please try again.")

def delete_expense():
    if not expenses:
        print("Invalid Choice")
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        display_expense(expense)

    try:  
        choice = int(input("Enter the expense number to delete: "))
        index = choice - 1
        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(index)
            print("Expense deleted successfully")
            display_expense(deleted)
        else:
            print("Invalid Number")
    except ValueError:
        print("Please Enter a Valid number.")


    
def update_expenses():
    if not expenses:
        print("No expenses found.")
        return
    for index, expense in enumerate(expenses, start=1):
        print(f"\nExpense {index}")
        display_expense(expense)
    
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
                   print("Category updated successfully.")
                elif update_choice in ("amount","2"):
                    new_amount =float(input(f"Enter your new Amount:({currency})"))
                    if new_amount > 0:
                      expense["amount"] = new_amount
                    else:
                      print("Amount must be greater than zero.")
                    expense["amount"] = new_amount
                    print(f"Amount updated successfully to {currency}{new_amount}")


                elif update_choice in ("description","3"):
                    new_description = input("Enter your new description:").strip().title()
                    expense["description"] = new_description
                    print("Description updated successfully.")
                elif update_choice in ("back","4"):
                    break
                else:
                    print("No Expense found")
            print("\nUpdated Expense:")
            display_expense(expense)

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def total_amount():
    pass


def total_savings():
    pass


def remaining_budget():
    pass


def main():
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
        print("8. Total Amount")
        print("9. Total Savings")
        print("10. Remaining Budget")
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
                total_amount()

            elif choice == 9:
                total_savings()

            elif choice == 10:
                remaining_budget()

            elif choice == 11:
                print("Exiting the program. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 11.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


   

main()
