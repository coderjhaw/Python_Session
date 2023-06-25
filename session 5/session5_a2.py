list_num = [1, 2, 3, 2, 4, 2, 5, 6, 2, 7]

# Append 10 to the end of the list
list_num.append(10)
print("1. Append 10: " + str(list_num))

# Insert 5 at the beginning of the list
list_num.insert(0, 5)
print("2. Inserted 5 at the beginning: " + str(list_num))

# Remove number 3
# .remove() since given is specific value 
list_num.remove(3)
print("3. Removed 3 from the list: " + str(list_num))

# Count occurrences of number 2
number_of_two = list_num.count(2)
print(f"4. Number 2 appear {number_of_two} times in the list : {list_num}")

# Sort in ASC order
list_num.sort()
print("5. List sorted in ascending order: " + str(list_num))

# Reverse order of the list
# list_num.reverse()
# list_num.sort(reverse=True)
print("6. Reverse order of list : " + str(sorted(list_num, reverse=True)))


