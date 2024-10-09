import random
def gusscharecter(lenght,word):
    attempts = 10
    print("ok now you should guess a charecter and im ganna tell you if the word has it\nthere are :")
    print(lenght * "_ ")
    found_charecterlist = []
    while attempts > 0:
        try:
            guess = input("guess a charecter: ").lower()
            if guess in word and not(guess in found_charecterlist):
                print(f"yes the word has the charecter {guess}")
                found_charecterlist.append(guess)
                print(f"u have found so far is :{found_charecterlist}")
                attempts -= 1
            else:
                print(f"no the word does not have the charecter {guess} or u have found this one before")
                print(f"u have found so far is :{found_charecterlist}")
                print(f"you have {attempts - 1}  attemts remaining")
                attempts -= 1

        except ValueError:
            print("Invalid input. Please enter a charecter.")

def guess_length(length):
    attempts = 4
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
            gusscharecter(len(word),word)

if __name__ == "__main__":
    main()