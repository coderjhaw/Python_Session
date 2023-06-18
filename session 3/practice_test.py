# num1 = int(input("First integer: "))
# num2 = int(input("Second integer: "))

# if num1 == num2:
#     print(f"{num1} is equal to {num2}")
# elif num1 > num2:
#     print(f"{num1} is larger than {num2}")
# else:
#     print(f"{num2} is larger than {num1}")

number = 3

if number%3 == 0 and number%5 == 0:
    print("FizzBuzz")
elif number%3 == 0:
    print("Fizz")
elif number%5 == 0:
    print("Buzz")
else:
    print(number)