def set_budget():
##choose currency:
    print("1.INR")
    print("2.USD")
    print("3.GBP")
    print("4.EUR")


    choice = input("Enter your Currency:").strip().lower()
   
       
    if choice == "inr"or choice=="1":
       choice ="₹"
       print("You choose INR (Indian Rupee) ")

    elif choice == "usd"or choice=="2" :
       choice = "$"
       print("You choose US Dollar")
    elif choice == "gbp"or choice=="3":
        choice = "£"
        print("You choose British Pounds")
    elif choice == "eur" or choice=="4":
        choice = "€"
        print("You choose Euro")
    else:
         print("Please enter currency from the choice")
         return 
    
    try:
        money = int(input("Enter your Amount:"))
        print(f"Your budget is {choice} {money}")
        return money , choice
    except ValueError:
        print("Please enter a valid amount.")
    


    
    



def emergency_fund():
    #Ask user to create an emergency fund
    
        answer = input("Do you want to create an emergency fund? (Y/N): ").strip().lower()

        if answer in ("yes","y"):
            
            print("You Choose YES")
            try:
                 set_limit=int(input("Enter the extending limit you want :"))
                 print(f"Emergency fund set to:{set_limit}")
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
#Main Program
budget, currency = set_budget
if budget is not None:
    emergency=emergency_fund(currency)


def add_expense():
    pass


def view_expenses():
    pass


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
                set_budget()

            elif choice == 2:
                emergency_fund()

            elif choice == 3:
                add_expense()

            elif choice == 4:
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
