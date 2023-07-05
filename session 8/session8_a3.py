
numbers = input("Enter a positive integer number: ")
# print(sum([int(num) for num in numbers])) 

sum_int = 0
for number in numbers:
    sum_int += int(number)
print(sum_int)


