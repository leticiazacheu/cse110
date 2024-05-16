#W04 Prove: Project Milestone - Word Pzzle

import random

def guessing():
    secret_word = 'mosiah'
    word_length = len(secret_word)
    number_of_guesses = 0 # Initialize the guess count to 0
    guessed_word = '_' * word_length

    print('Welcome to the work guessing game!')

    while True:
        guess = input('What is your guess? ')
        number_of_guesses += 1

        if len(guess) != word_length:
            print('Invalid guess length. Please guess a word with', word_length, 'letters.')
            continue
        if guess.lower() == secret_word:
            print('Congratulations! You guessed it right!')
            print('It took you', number_of_guesses, 'guesses.')
            break
        hint = ''
        for i in range(word_length):
            if guess[i] == secret_word[i]:
                hint += guess[i].upper()
            elif guess[i] in secret_word:
                hint += guess[i].lower()
            else:
                hint += '_'

        print('Your guess was not correct.')
        print('Hint:', hint)
    again()

def again():
    if input('Continue? (y/n) ') == 'y':
        guessing()
    else:
        exit()

guessing()
