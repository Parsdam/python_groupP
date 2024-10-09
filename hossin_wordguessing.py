import random
def gusscharecter():
    print("you got it right")
def guess_length(length):
    attempts =4
    print(f"ok first you need to guess the length of the word.\nyou have {attempts} attempts to guess")

    while attempts > 0:
        try:
            guess = int(input("Please enter your guess: "))
        except ValueError:
            print("you must enter a number as your guess")
            continue

        if guess == length:
            print("congrats you got the length of the word")
            return 1
        elif guess > length:
            print("too big")
            attempts -= 1
        elif guess < length:
            print("too small")
            attempts -= 1
    return 0    

def randomword():
    words = ["rainbow", "apple", "orange", "administ",'rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
    return random.choice(words)

def main():
    print("hello wellcome to guess the word game!\n")
    want2paly = "Y"
    while want2paly == "Y":
        print("im thinking of a word ....")
        word = randomword()
        if guess_length(len(word)):
            gusscharecter()

if __name__ == "__main__":
    main()