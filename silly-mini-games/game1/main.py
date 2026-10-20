import random

guess = 0

print("Hello World")
print("Welcome to Sarah's silly mini games :D")

#game 1: Guess da number
print("Game 1: Guess the number")

game = input("Which game would you like to play?")

if game == "1":
    
    print("The genie has chosen a number between 1 and 10. Can you guess it in 3 tries?")
    
    def guess_number():
        number = random.randint(1, 10)
        for attempt in range(3):
            guess = int(input("Enter your guess:"))
            if guess < 1 or guess > 10:
                print("Atleast TRY to guess.. Hint: It's between 1 and 10.. Loser")
            elif guess == number:
                print("You guessed right !!! The number was indeed", number, "!!")
                return
            elif guess > number:
                print("A little too high there buddy.. Let's try again! You have", 2 - attempt, "tries left")
            else:
                print("A little too low! We're getting close tho trust.. You have", 2 - attempt, "tries left")
            
        else:
            print("The number was", number, ":( Better luck next time!")

guess_number()