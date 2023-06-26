import pwinput
user = {
    "username" : "",
    "password" : ""
}


print("User Registration")
print("-----------------")

username = input("Enter a username: ")
password = pwinput.pwinput("Enter a password: ")

user.update({
                "username": username,
                "password": password   
})

print("\n\nUser Login")
print("----------")

login_username = input("Enter your username: ")

if login_username == user["username"]:
    login_password = pwinput.pwinput("Enter your password: ")
    if login_password == user["password"]:
        print(f"Login successful. Welcome, {login_username}!")
    else:
        print("Invalid password")
else:
    print("Invalid username")


