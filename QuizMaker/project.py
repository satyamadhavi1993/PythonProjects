from bs4 import BeautifulSoup
from display_scores import display_score_board
import html
import json
from pyfiglet import Figlet
import random
import requests
import sys
from tabulate import tabulate


def main():
    print_message('Welcome')
    gameon = True

    while gameon:
        while True:
            category_index, category = get_category()
            difficulty = get_difficulty()
            questions = fetch_questions(category_index, difficulty)

            if questions:
                break
            else:
                print('The selected category/difficulty level is not available. Please select another one.\n')

        score = display_questions(questions)

        display_score_board(category, score)
        gameon = continue_playing()

    print_message('Goodbye')


def print_message(message):
    figlet = Figlet()
    figlet.setFont(font='slant')
    print(figlet.renderText(message))


def continue_playing():
    while True:
        choice = input("Do you want to continue playing (Y or N): ").strip().upper()
        print()
        if choice in ['Y', 'YES']:
            return True
        elif choice in ['N', 'NO']:
            return False
        else:
            print('Please enter valid choice (Y or N)')


def fetch_all_categories():
    response = requests.get('https://opentdb.com/api_config.php')
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        select_element = soup.find("select", {"name": "trivia_category"})
        categories = {}
        for option in select_element.find_all("option"):
            categories.update({option.get_text(): option["value"]})
        return categories
    else:
        print("Failed to retrieve categories. Status code:", response.status_code)
        sys.exit()


def get_category():
    print('Select a category from the below list\n')
    categories = fetch_all_categories()

    for index, category in enumerate(categories):
        print(f'{index + 1} - {category}')
    print()

    while True:
        try:
            category_index = int(
                input('Please enter the index of the category you want (1 - 25): '))
            if 1 <= category_index <= len(categories):
                break
            else:
                print('Invalid input. Please enter a number between 1 and 25.')
        except ValueError:
            print('Invalid input. Please enter a number.')
    print()
    category = list(categories.keys())[category_index - 1]
    return categories[category], category


def get_difficulty():
    while True:
        difficulty_levels = {'E': 'easy', 'M': 'medium', 'H': 'hard', 'EASY': 'easy',
                             'MEDIUM': 'medium', 'HARD': 'hard', 'A': 'any', 'ANY': 'any'}
        difficulty = input(
            "Select difficulty level (E for Easy, M for Medium, H for Hard, A for Any): ").strip().upper()
        if difficulty in difficulty_levels:
            return difficulty_levels[difficulty]
        else:
            print('Please select a valid difficulty level (E, M, H, or A).')


def fetch_questions(category, difficulty):
    url = f'https://opentdb.com/api.php?amount=10&type=multiple'
    if not category == 'any':
        url += f'&category={category}'
    if not difficulty == 'any':
        url += f'&difficulty={difficulty}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        questions = data.get('results', [])
        random.shuffle(questions)
        return questions
    else:
        print("Failed to retrieve questions. Status code:", response.status_code)
        sys.exit()


def display_questions(questions_list):
    score = 0
    for question_number, question in enumerate(questions_list):
        print()
        correct_option_index = display_question(question_number, question)
        print()
        user_answer = get_user_answer()
        if user_answer == correct_option_index:
            print('Correct answer !!\n')
            score += 1
        else:
            print(f'Correct answer is: {correct_option_index}. {html.unescape(question["correct_answer"])}\n')
    return score


def display_question(question_number, question):
    print(f'{question_number + 1}. {html.unescape(question["question"])}\n')
    options = [question['correct_answer']] + question['incorrect_answers']
    random.shuffle(options)
    correct_option_index = None
    for index, option in enumerate(options):
        options_index = chr(97 + index)
        print(f'    {options_index}. {html.unescape(option)}')
        if option == question['correct_answer']:
            correct_option_index = options_index
    return correct_option_index


def get_user_answer():
    while True:
        answer = input('Enter your answer: ').lower()
        if answer in ['a', 'b', 'c', 'd']:
            return answer
        else:
            print('Please select an option from (a, b, c, or d): ')


if __name__ == "__main__":
    main()
