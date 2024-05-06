from random import shuffle

# Shuffle ball game
list1 = ['', 'O', '']


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = None
    while guess not in ['0', '1', '2']:
        guess = input("Enter your guess: ")
    return int(guess)


def ball_is_in_guessed_position(shuffledlist, guess):
    if shuffledlist[guess] == 'O':
        print(f"Correct, ball is in {shuffledlist}")
    else:
        print(f"Wrong, ball is in {shuffledlist}")


ball_is_in_guessed_position(shuffle_list(list1), player_guess())
