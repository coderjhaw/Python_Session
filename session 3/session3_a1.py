user = input("Enter a string: ")
string_length = len(user)
upcase = user.upper()
lowcase = user.lower()
reverse = user[::-1]
modified = user.replace(user[0], user[string_length-1])


print(f"String length: {string_length}")
print(f"Uppercase: {upcase}")
print(f"Lowercase: {lowcase}")
print(f"Reversed String: {reverse}")
print(f"Modified String: {modified}")

