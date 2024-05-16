import random

def generate_secret_word():
    words = ['mosiah', 'python', 'guitar', 'zeppelin', 'wonder']
    return random.choice(words)

def get_guess(word_length):
    while True:
        guess = input('What is your guess? ')
        if len(guess) != word_length:
            print('Invalid guess length. Please guess a word with', word_length, 'letters.')
        else:
            return guess.lower()

def provide_hint(guess, secret_word):
    hint = ''
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            hint += guess[i].upper()
        elif guess[i] in secret_word:
            hint += guess[i].lower()
        else:
            hint += '_'
    return hint

def play_game():
    secret_word = generate_secret_word()
    word_length = len(secret_word)
    number_of_guesses = 0

    print('Welcome to the word guessing game!')

    while True:
        guess = get_guess(word_length)
        number_of_guesses += 1

        if guess == secret_word:
            print('Congratulations! You guessed it right!')
            print('It took you', number_of_guesses, 'guesses.')
            break

        hint = provide_hint(guess, secret_word)

        print('Your guess was not correct.')
        print('Hint:', hint)

    if input('Continue? (y/n) ') == 'y':
        play_game()
    else:
        exit()

play_game()