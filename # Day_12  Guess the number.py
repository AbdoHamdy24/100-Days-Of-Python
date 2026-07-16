# Guess the number
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")

difficulty = input("Choose a difficulty: Type 'easy' or 'hard' >>> ")
number = random.randint(1,100)

def easy():
    guess = int(input("Make a guess: "))
    attempts = 10

    while guess != number and attempts > 0 :
        attempts -= 1     
        if attempts == 0 :
            print("You lose, You've run out of guesses.")
            return    
        if guess > number:
            print("Too high!, guess again.")
        elif guess < number:
            print("Too low!, guess again.")
        print(f"You have a {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: ")) 
    if guess == number:
            print(f"{number} is the Correct guess, congratulations!")           
        
def hard():
    guess = int(input("Make a guess: "))
    attempts = 5

    while guess != number and attempts > 0 :
        attempts -= 1     
        if attempts == 0 :
            print("You lose, You've run out of guesses.")
            return    
        if guess > number:
            print("Too high!, guess again.")
        elif guess < number:
            print("Too low!, guess again.")
        print(f"You have a {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
    if guess == number:
            print(f"{number} is the Correct guess, congratulations!")    
                    
if difficulty == 'easy':
    print(f"You have a 10 attempts remaining to guess the number.")
    easy()
elif difficulty == 'hard':
    print(f"You have a 5 attempts remaining to guess the number.")
    hard()
else:
    print("Wrong choise!")        