# Write your code here
from random import choice
import sys
import string

print("H A N G M A N")

word_list = ['python', 'java', 'kotlin', 'javascript']
random_word = choice(word_list)
temp_string = list("-" * len(random_word))
tries = 0
guesses = []


def menu():
    while True:
        menu_input = input('Type "play" to play the game, "exit" to quit: ')
        if menu_input == "play":
            break
        else:
            sys.exit(0)


def results_test(temp_string, tries=0):
    if "-" not in temp_string or tries == 8:
        if "".join(temp_string) == random_word:
            print("You guessed the word!")
            print("You survived!\n")
            menu()
        else:
            print("You are hanged!\n")
            menu()


def print_temp(temp_string):
    print("\n" + "".join(temp_string))
    results_test(temp_string)


def tries_count(temp_string):
    global tries
    tries += 1
    results_test(temp_string, tries)


def check_for_duplicates(temp_string, user_input):
    if user_input in temp_string:
        print("You already typed this letter")
        # tries_count(temp_string)
        print_temp(temp_string)
    else:
        count = random_word.count(user_input)
        while count != 0:
            for position, character in enumerate(random_word):
                if user_input == character:
                    temp_string[position] = user_input
                    count -= 1
            if count == 0:
                print_temp(temp_string)


def user_input_test(user_input):
    if len(user_input) != 1:
        print("You should input a single letter")
        print_temp(temp_string)
        return False
    elif user_input not in string.ascii_lowercase:
        print("It is not an ASCII lowercase letter")
        print_temp(temp_string)
        return False
    return True


menu()

print_temp(temp_string)

while True:
    user_input = input("Input a letter: ")
    if user_input_test(user_input) == True:
        guesses.append(user_input)
        if guesses.count(user_input) > 1:
            print("You already typed this letter")
            print_temp(temp_string)
        elif random_word.find(user_input) == -1:
            print("No such letter in the word")
            tries_count(temp_string)
            print_temp(temp_string)
        else:
            check_for_duplicates(temp_string, user_input)
