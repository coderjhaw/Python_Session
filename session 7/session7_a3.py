print("Welcome to the Simple Calculator!")
while True:
    user_input = input("\nEnter 'x' to exit or press Enter to continue.\n")
    
    # Exit the program if user enter 'x'
    # then continue when press Enter
    if user_input.lower() == 'x':
        print("Goodbye!")
        break
    
    first_num  = int(input("Enter the first number: "))
    operator   = input("Enter the operator (+, -, *, /): ")
    second_num = int(input("Enter the second number: "))
    
    if operator == '+':
        print(f"{first_num} + {second_num} = {first_num + second_num}")
    elif operator == '-':
        print(f"{first_num} - {second_num} = {first_num - second_num}")
    elif operator == '*':
        print(f"{first_num} * {second_num} = {first_num * second_num}")
    elif operator == '/':
        if second_num != 0:
            print(f"{first_num} / {second_num} = {first_num / second_num}")
        else:
            print("\n--------------")
            print("UNDEFINED! Cannot divide number by zero!\n")
    else:
        print("Wrong input of operation. Please try again!")

