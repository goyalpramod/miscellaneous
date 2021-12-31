import random

def hangman():
    word = random.choice(["apple", "pizza", "dog", "tree", "phone", "sun", "pineapple", "eight", "word", "running"])
    validLetters = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessMade = ""

    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guessMade:
                main += letter
            else:
                main += "_" + ""

        if word == main:
            print(main)
            print("you win")
            break

        print("guess the word", main)
        guess = input()



        if guess not in word:
            turns -= 1
            if turns == 9:
                print("9 turns left")
                print(" -------------- ")
            if turns == 8:
                print("8 turns left")
                print(" -------------- ")
                print("        0       ")
            if turns == 7:
                print("7 turns left")
                print(" -------------- ")
                print("        0       ")
                print("        |       ")
            if turns == 6:
                print("6 turns left")
                print(" -------------- ")
                print("        0       ")
                print("        |       ")
                print("       /        ")
            if turns == 5:
                print("5 turns left")
                print(" -------------- ")
                print("        0       ")
                print("        |       ")
                print("       / \      ")
            if turns == 4:
                print("4 turns left")
                print(" -------------- ")
                print("      \ 0       ")
                print("        |       ")
                print("       / \      ")
            if turns == 3:
                print("3 turns left")
                print(" -------------- ")
                print("      \ 0 /     ")
                print("        |       ")
                print("       / \      ")
            if turns == 2:
                print("2 turns left")
                print(" -------------- ")
                print("      \ 0 /|     ")
                print("        |       ")
                print("       / \      ")
            if turns == 1:
                print("1 turn left")
                print(" -------------- ")
                print("      \ 0_/|    ")
                print("        |       ")
                print("       / \      ")
            if turns == 0:
                print("You lose")
                break

        if guess in validLetters:
            guessMade += guess
        else:
            print("Enter a valid character")
            guess = input()


name = input("Enter your name.")
print("Welcome", name)
print("----------------")
print("Try to guess the word in less than 10 attempts")
hangman()
