from art import logo
import random
print(logo)
print("WELCOME TO OUR NUMBER GUESSING GAME")
print("I am thinking of a number between 1 to 100")
random_number = random.randint(1,100)
difficulty = input("Enter on what difficulty you want to play 'EASY' or 'HARD' : ")
diff = difficulty.lower()
if diff == "easy":
    tries = 10
elif diff== "hard":
    tries = 5
else:
    print("enter valid difficulty")
print(f"You have {tries} no of attempts left.")

while tries>0:
    user_number = int(input("Make a Guess : "))
    if user_number>random_number:
        print("too high")
        print("guess again")
        tries = tries-1
        print(f"You have {tries} no of attempts left.")
    elif user_number<random_number:
        print("Too low ")
        print("Guess again")
        tries = tries-1
        print(f"You have {tries} no of attempts left.")
    else:
        print(f"You guessed corerectly the number was {random_number}")
        tries = 0 