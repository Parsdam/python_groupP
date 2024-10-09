import random
def guesstheword(word):
    attempts = 3
    print("ok now try to guess the word")
    for i in range(attempts):
        if word == input("what do u think the word is : "):
            print("congrats ")
    


def gusscharecter(lenght,word):
    attempts = 10
    print("ok now you should guess a charecters in the word and im ganna tell you if the word has it or not\nthere are :")
    print(lenght * "_ " + " charecters")
    found_charecterlist = []
    while attempts > 0:
        try:
            guess = input("guess a charecter: ").lower()
            if guess in word and not(guess in found_charecterlist):
                print(f"yes the word has {word.count(guess)} of the charecter {guess}")
                found_charecterlist.append((word.count(guess),guess))
                print(f"u have found so far is :{found_charecterlist}")
                attempts -= 1
                print(f"you have {attempts}  attemts remaining")
            else:
                print(f"no the word does not have the charecter {guess} or u have found this one before")
                print(f"what u have found so far is :{found_charecterlist}")
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
    words = ["rainbow", "apple", "orange", "administ",'rainbow',
            'computer', 'science', 'programming',
            'python', 'mathematics', 'player', 'condition',
            'apple', 'banana', 'cherry', 'date', 'elderberry',
            'fig', 'grape', 'honeydew', 'kiwi', 'lemon', 'mango',
            'nectarine', 'orange', 'pear', 'plum', 'quince', 'raspberry',
            'strawberry', 'tangerine', 'watermelon'
            'reverse', 'water', 'board', 'geeks']
    return random.choice(words)

def main():
    print("hello wellcome to guess the word game!\n")
    want2paly = "Y"
    while want2paly.upper() == "Y":
        print("im thinking of a word ....")
        word = randomword()
        if guess_length(len(word)):
            gusscharecter(len(word),word)
            guesstheword(word)
        want2paly = input("do you want to play again : Y/N ")
    #say it was fun palying with you if thay dont want to play anymore
if __name__ == "__main__":
    main()