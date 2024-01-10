import random

secret_number = random.randint(1, 10)

print("Welcome to the number guessing game:")
print("You must guess a number between 1 and 10")

number = (int(input("Your guess is: ")))

print(number)

if number == secret_number:
    print("Well done you have guessed the secret number :)")
else:
    print("Oh no looks like you didn't get the number :(")
    print("The secret number was {}".format(secret_number))
