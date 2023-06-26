users = {
    1 : {
        "name"    : "",
        "age"     : 22,
        "address" : "Paranaque City, NCR",
        "hobby"   : "Table tennis"
    },
    2 : {
        "name"    : "",
        "age"     : 33,
        "address" : "Maasin City, Southern Leyte",
        "hobby"   : "Mobile Legends"
    }, 
    3 : {
        "name"    : "",
        "age"     : 27,
        "address" : "Cebu City, Cebu",
        "hobby"   : "Basketball"
    },
    4 : {
        "name"    : "",
        "age"     : 29,
        "address" : "Makati City",
        "hobby"   : "Forex Trading"
    }
}

user_input = int(input("Enter a number: "))

if user_input in users:
    print("\nUser found! Name:", users[user_input]["name"])
    user_preference = input("Enter your preference\n(A: age, B: address, C: hobby)\n")
    if user_preference.upper() == 'A':
        print("Age is ", users[user_input]['age'])
    elif user_preference.upper() == 'B':
        print("Address: ", users[user_input]['address'])
    elif user_preference.upper() == 'C':
        print("Hobbies :", users[user_input]['hobby'])
    else:
        print("Invalid preference")
else:
    print(f"User {user_input} not found!")