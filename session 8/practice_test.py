n = int(input("Enter a number: "))
sum = 0
expression = ""

for i in range(1, n+1):
    sum += i
    if i != n:
        expression += str(i) + " + "
    else:
        expression += str(i)

print("\n--------------------")
print(f"The answer is {sum}")
print(f"{expression} = {sum}")