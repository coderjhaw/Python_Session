import time
import database as db
import random
from datetime import datetime
import string


# display Balance / inquire balance
def inquire_balance(current_user):
    first_name = db.data[current_user]["first_name"] 
    last_name = db.data[current_user]["last_name"]
    account_balance = db.data[current_user]["account_balance"]

    return f"\n\tFirst Name: {first_name}\n\tLast Name: {last_name}\n\tRemaining Balance: {account_balance:,.2f}"


# USER REGISTRATION 
def register_user(username, password, first_name, last_name, account_balance):
    db.data.update({username : {
                        "password"        : password,
                        "first_name"      : first_name,
                        "last_name"       : last_name,
                        "account_balance" : account_balance
                    }})
    
# USER LOGIN 
def login_user(username, password):
    if username in db.data:
        if password == db.data[username]["password"]:
            return "Successful"
        else:
            return "Invalid credentials"
    else:
        return f"No user {username} found"

# DEPOSIT MONEU IN THE ACCOUNT
def deposit_money(username, amount):
    db.data[username]["account_balance"] += amount
    
# TRANSFER FUNDS TO OTHER ACCOUNT
def transfer_funds(current_user, recipient_username, amount_to_transfer):
    if recipient_username in db.data:
        if db.data[current_user]["account_balance"] >= amount_to_transfer:
            db.data[current_user]["account_balance"] -= amount_to_transfer # this will deduct the funds from sender
            db.data[recipient_username]["account_balance"] += amount_to_transfer # add funds to the recipient
            return "Successful"
        else:
            return "\n -> Sorry, you have insufficient Balance to transfer funds"
    else:
        return " -> Username not found!"

# DELETE ACCOUNT 
def delete_account(username, password):
    if username in db.data:
        if password == db.data[username]["password"]:
            del db.data[username]
            print("Account deleted successfully!")
        else:
            return " -> Invalid password"
    else:
        return " -> User not in database"

# function for generating receipt code
def ref_code():
    current_date = datetime.now().strftime("%m%d%y")
    random_number = "{:04d}".format(random.randint(1, 5000))
    # this will return T******, where T means Transfer funds transaction is made by the user
    receiptcode = str(current_date) + str(random_number) + random.choice(string.ascii_letters.upper()) + random.choice(string.ascii_letters.upper())
    return receiptcode


def begin_end():
    print("-" * 50)


def loader():
    print(".", end="", flush=True)
    time.sleep(1)
    print(".", end="", flush=True)
    time.sleep(1)
    print(".")