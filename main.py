import random


# programm
print("Hello, friend")
random_number = random.randint(1, 10)
max_tries = 10
user_tries = 0
score = 1000

while True:

    user_input = input("Guess number: ")
    user_tries += 1
    print("try left ", (max_tries - user_tries))

    if user_input == "stop":
        print("the guessed number was", random_number)
        break
    try:
        user_input = int(user_input)
    except ValueError as ex:
        print("The hidden number must contain only numbers")
        continue



    if random_number == user_input:
        print("Your score", (score *(max_tries - user_tries + 1) / (max_tries)))
        break
    else:
        if random_number > user_input:
            print("The hidden number is greater")
        else:
            print("The hidden number is less")

input("Press ENTER to exit")

