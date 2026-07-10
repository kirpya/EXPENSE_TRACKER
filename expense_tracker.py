
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
 
    while True:
      
      category =input("Enter the expense category:")
      category=category.title()
      

      if not category:
          print("Enter category:")
          continue


      try:
       amount = float(input("Enter the expense amount you want to add :"))
      except ValueError:
          print("Error ! Enter a valid number")
          continue
      
     
      
      description=input("Enter a description :")
      description = description.strip()
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
      }
      expenses.append(expense)

      print ("Expense added successfully ")
      break
          


    


def view_expenses():
    if not expenses:
        print("NO Expense found")
    else:
        for expense in expenses:
            print(f"Category        :{expense['category']}")
            print(f"Amount          :{expense['amount']}")
            print(f"Description     :{expense['description']}")
            print("*" * 30)
    


def search_expenses():
    pass


def delete_expense():
    pass


def update_expenses():
    pass


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
