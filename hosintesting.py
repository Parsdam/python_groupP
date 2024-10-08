import random
score = 0
def playgame(min_number, max_number, max_tries):
    attempt = 0
    number_to_guess = random.randint(min_number, max_number)
    print(f"I'm thinking of a number between {min_number} and {max_number}. You have {max_tries} tries.")
    
    for attempt in range(max_tries - 1):
        try:
            guess = int(input("whats youre guess ? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            attempt -= 1
            continue

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempt+1} attempts.")
            score += 1
            break
        elif guess < number_to_guess:
            print("Too low!")

        elif guess > number_to_guess:
            print("Too high!")
        
        elif guess > max_number or guess < min_number :
            print("Invalid input. Please enter a number.") 
            attempt -= 1
        
def main():

    print("welcome to my gussing game! \n ------------------------------------------------------------")
    while True:
        try:
            difficulty_lvl = int(input("Choose your difficulty level (you will have 4 chancess to guess correctly): \n1. Easy (1-10) \n2. Medium (1-100) \n3. Hard (1-1000) \n ??? "))
            break
        except ValueError:
            print("Invalid difficulty level selected. Please enter a number.")
            continue

    match (difficulty_lvl):
        case (1):
            print("Easy mode selected")
            playgame(1,10,2)
        case (2):
            print("Medium mode selected")
            playgame(1,100,5)
        case (3):
            print("Hard mode selected")
            playgame(1,1000,10)
        case (4):
            print("custom mod selected")
            playgame(int(input("\nenter minimum number: ")),int(input("\nenter maximum number: ")),int(input("\nenter tries number: ")))
        case _:
            print("Invalid difficulty level selected")
if __name__ == "__main__":
    main()