import time
import database as db
import modules  as md
import pwinput as pw

# THIS LINE HERE IS FOR IMPORTING PYTHON FILE FROM DIFFERENT FOLDER
import sys
sys.path.insert(0, 'D:\pythonfiles\python_session\python_session')
from session_10.passwordchecker import checkPassword as ck

# RECEIPT (DATE + RANDOM NUMBER)
# 1. REGISTER USER ACCOUNT
    # A. password checker
# 2. LOGIN USER ACCOUNT
    # A. DEPOSIT
    # B. WITHDRAW
    # C. TRANSFER FUNDS
    # D. LOG OUT

while True:
    print("-" * 15 + " WELCOME TO BANCASH " + "-" * 15)
    print("\nHow may I help you ?\n\n1. Register User\n2. Login Account\n3. Exit")


    user_response = int(input("\n >>  "))

    # REGISTER NEW USER HERE
    if user_response == 1:
        md.begin_end()
        print("-" * 15 + " USER REGISTRATION " + "-" * 15)
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        username = input("Please enter a username: ")
        account_balance = float(input("Please enter you initial deposit: "))

        # THIS IS CHECKED BY THE PASSWORD CHECKER FROM THE SESSION 10 FOLDER
        while True:
            password = pw.pwinput("Please setup a password: ")
            c_password = pw.pwinput("Confirm password: ")

            if password == c_password:
                if ck(password) == True:
                    md.register_user(username, password, first_name, last_name, account_balance)
                    break
                else:
                    print("Please provide a strong password\n\t1. at least 10 characters\n\t2. at least 1 Uppercase\n\t3. at least 1 lowercase")
                    print("\t4. at least 1 number\n\t5. at least 1 symbol")
            else:
                print("Passwords do not match!")
        print("\nSuccessfully registered!")
        md.begin_end()
    
    # LOGIN EXISTING ACCOUNT
    elif user_response == 2:
        current_user = ""
        md.begin_end()
        while True:   
            username = input("Username: ")
            password = input("Password: ")

            if md.login_user(username, password) == "Successful":
                current_user = username
                print(f"\nSuccessfully logged in as {username}")
                md.loader()
                break
            else:
                print(md.login_user(username, password))
        md.begin_end()
        while True:
            print("\n\t1. Inquire Balance\n\t2. Deposit Money\n\t3. Transfer Funds\n\t4. Delete Account\n\t5. Logout\n")
            user_response = int(input("Select a transaction: "))

            # INQUIRE ACCOUNT REMAINING BALANCE
            if user_response == 1:
                md.begin_end()
                print(f"BALANCE INQUIRY\t\t\t\t{current_user}")
                md.begin_end()
                print(md.inquire_balance(current_user)) 
                md.begin_end()
                enter = input("\nPress enter to continue . . .")
            
            # ADD FUNDS / DEPOSIT MONEY
            elif user_response == 2:
                md.begin_end()
                print(f"DEPOSIT MONEY\t\t\t\t{current_user}")
                md.begin_end()
                amount = float(input("Please enter amount you want to deposit: "))
                md.deposit_money(current_user, amount)
                balance = db.data[current_user]["account_balance"]
                print("\nDeposit Successful")
                # Here I have formatted the money in `1,000.00` to be more readable
                print(f"Your new balance: {balance:,.2f}\n")
                print(f"Transaction reference no. : {md.ref_code()}")
                md.begin_end()
                enter = input("\nPress enter to continue . . .")

            # TRANSFER FUNDS TO EXISTING USER IN DATABASE
            elif user_response == 3: 
                while True:
                    md.begin_end()
                    print(f"TRANSFER FUNDS\t\t\t\t{current_user}")
                    md.begin_end()
                    recipient = input("Enter the receiver's username: ")
                    amount = float(input("Enter the amount you want to transfer: "))
                    user_prompt = input(f"You are transferring funds to `{recipient}`, do you wish to continue? y/n: ")
                    if user_prompt.lower() == 'y':
                        if md.transfer_funds(current_user, recipient, amount) == "Successful":
                            md.loader()
                            print("\nTransfer Successful!")
                            new_balance = db.data[current_user]["account_balance"]
                            print(f"\nYour new balance is {new_balance:,.2f}")
                            print(f"Transaction reference no. : {md.ref_code()}")
                            md.begin_end()
                            enter = input("\nPress enter to continue . . .")
                            break
                        else:
                            print(md.transfer_funds(current_user, recipient, amount))
                            md.begin_end()
                            enter = input("\nPress enter to continue . . .")
                            break
                    elif user_prompt.lower() == 'n':
                        break
                    else:
                        print("Wrong option")
                    md.begin_end()
                    enter = input()
            # DELETE USER ACCOUNT AND INFOS
            elif user_response == 4:
                md.begin_end()
                print("-> DELETE ACCOUNT")
                md.begin_end()
                while True:
                    user_prompt = input("This will delete all the account information, continue ? y/n:  ")
                    if user_prompt.lower() == 'y':
                        del db.data[current_user]
                        md.loader()
                        print("Account successfully deleted!")
                        enter = input("Press enter to continue . . .")
                        break
                    elif user_prompt == 'n':
                        break
                    else:
                        print('wrong choice')
                md.begin_end()
                break
            # EXIT / GO TO THE MAIN MENU
            elif user_response == 5:
                print(f"Bye, {current_user}")
                break
            else:
                print("Invalid option.")

    elif user_response == 3:
        print(f"Good Bye!!")
        md.begin_end()
        md.loader()
        break

    else:
        print("Invalid Option! Try again...")
    