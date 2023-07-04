import random

random_num = random.randint(1, 20)

lives = 3
for tries in range(lives):
    print("Tries left: " + str(lives - tries))
    guess = int(input("Take a guess: "))
    if guess > random_num:
        print("Too high!")
    elif guess < random_num:
        print("Too low!")
    else:
        print("\n"  + "-" * 8)
        print("Congratulations! You guessed the number correctly!")
        break # exit loop after correct answer is found
else:
    print("\n"  + "-" * 8)
    print("You Lose")


