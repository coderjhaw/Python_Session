print("What would you like to convert?\nA. cm to inches\nB. inches to cm")
answer = input ("Enter your answer: ")

if answer.upper() == "A": # forcing input to uppercase
    print("You chose cm to inches")
    length = float(input("Enter the length: "))
    print(f"{length} cm is equal to {length/2.54} inche/s")
elif answer.upper() == "B": # forcing input to uppercase
    print("You chose inches to cm")
    length = float(input("Enter the length: "))
    print(f"{length} inche/s is equal to {length*2.54} cm")
else:
    print("Invalid answer")