import random

print("HI wlecome to the game. This is a number guessing game. \nYou got 7 chances to guess the number. Let's start the game.")

number_to_guess = random.randrange(100)

chances = 7

quess_counter = 0

while quess_counter < chances:
    
    quess_counter += 1
    my_guess = int(input("Enter your guess: "))
    
    if my_guess == number_to_guess:
        print(f"Congratulation! You got the number in {quess_counter} guesses.")
        break
    
    elif quess_counter >= chances and my_guess != number_to_guess:
        print(f"Sorry! You lost the game. The number was {number_to_guess}")
        
    elif my_guess < number_to_guess:
        print("Your guess is less than the number. Try again.")
    
    elif my_guess > number_to_guess:
        print("Your guess is greater than the number. Try again.")