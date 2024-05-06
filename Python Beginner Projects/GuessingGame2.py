import random


def user_guess(limit):
    random_number = random.randint(1, limit+1)
    number_of_guesses = 0
    guess = 0
    while guess != random_number:
        while True:
            try:
                guess = int(input(f'Please enter your guess between 1 - {limit}: '))
            except ValueError:
                print('Please enter a valid number')
            else:
                if guess in range(1, limit+1):
                    break
        number_of_guesses += 1
        if guess < random_number:
            print('Sorry, try again. Your guess is low')
        elif guess > random_number:
            print('Sorry, try again. Your guess is high')

    print(f'Congratulations, you guessed {guess} correctly and it took {number_of_guesses} guesses')


user_guess(50)
