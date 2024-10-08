import random

print("hello and welcome to my gussing game!")

deficalty = int(input("how hard do you want it to bew: "))
number_to_guess = random.randrange(1, deficalty)
win = False

guss_counter = 0
chance = 4
point = 0

print("------------------------------------------------------")

while guss_counter <= chance:
    guss_counter += 1
    guess = int(input("pls inter ur guess : "))

    if guess == number_to_guess:

        print(f"the number {guess} is corecct congrats \n it took you {guss_counter} attempts")
        win = True
        break
        

    elif guess > number_to_guess:
        print(f"the number {guess} in too big try smaller numbers")

    elif guess < number_to_guess:
        print(f"the number {guess} is too small try a bigger number")


if win:
    point += 1
    print(f"__________________________________________________ \ncongrats ur point is {point}")
    print("do u wanna start agian")
    win = False
else:
    print("ur out of trys do u wanna start again")