import random

print("Welcome to the Number Guessing Game")

random_num = random.randint(1, 20)

tries = 3

while tries > 0:
    print("Tries: " + str(tries))
    guess = int(input("Take a guess: "))
    if guess > random_num:
        print("Too High!")
        tries -= 1
    elif guess < random_num:
        print("Too Low!")
        tries -= 1
    else:
        print("\n------------")
        print(f"Congratulations! You guessed the {random_num} correctly!")
        break
else:
    print("\n--------------")
    print(f"Guessing Over! The number is {random_num}.")