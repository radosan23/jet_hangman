from random import choice

won, lost = 0, 0


def play():
    global won, lost
    words = ['python', 'java', 'swift', 'javascript']
    word = choice(words)
    guessed = set()
    bad_tries = set()
    attempts = 8
    while attempts > 0:
        uncovered = word
        for i in uncovered:
            if i not in guessed:
                uncovered = uncovered.replace(i, '-')
        print('\n' + uncovered)
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('Please, input a single letter.')
        elif not letter.isalpha() or not letter.islower():
            print('Please, enter a lowercase letter from the English alphabet.')
        elif letter in set(word) and letter not in guessed:
            guessed.add(letter)
        elif letter in guessed or letter in bad_tries:
            print("You've already guessed this letter.")
        else:
            bad_tries.add(letter)
            attempts -= 1
            print("That letter doesn't appear in the word.")
        if set(word) == guessed:
            break
    if set(word) == guessed:
        won += 1
        print(f'\nYou guessed the word {word}!\nYou survived!')
    else:
        lost += 1
        print('\nYou lost!')


def score():
    print(f'\nYou won: {won} times\nYou lost: {lost} times')


print('H A N G M A N')
menu = ''
while menu != 'exit':
    menu = ''
    while menu not in ['play', 'results', 'exit']:
        menu = input('\nType "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
        if menu == 'play':
            play()
        elif menu == 'results':
            score()
