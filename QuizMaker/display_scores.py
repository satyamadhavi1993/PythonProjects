import csv
import emoji
import os
import pyfiglet
from tabulate import tabulate


def display_score_board(category, current_score):
    file_name = 'scores.csv'
    create_new_file(file_name)
    previous_score = read_scores(file_name, category, current_score)
    display_score(category, current_score, previous_score)


def create_new_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['category', 'highest_score'])


def read_scores(file_name, category, current_score):
    scores = {}
    with open('scores.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            scores[row['category']] = int(row['highest_score'])

    if category in scores:
        previous_score = scores[category]
        if scores[category] < current_score:
            scores[category] = current_score
            update_scores(file_name, scores)
        return previous_score
    else:
        scores[category] = current_score
        update_scores(file_name, scores)
        return None


def update_scores(file_name, scores):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['category', 'highest_score'])
        for category, highest_score in scores.items():
            writer.writerow([category, highest_score])


def display_score(category, current_score, previous_score):
    print(pyfiglet.figlet_format('Score Board', font='small'))
    congrats_message = ""
    if previous_score == None:
        score_table = [category, current_score]
        headers_value = ['Category', 'Your Score']
    else:
        score_table = [category, current_score, previous_score]
        headers_value = ['Category', 'Your Score', 'Highest Score']

        if current_score > previous_score:
            headers_value[2] = 'Previous Highest Score'
            congrats_message = f'{emoji.emojize(":trophy:", language="alias")} Congratulations! You achieved the highest score in this category!'
        elif current_score == previous_score:
            headers_value[2] = 'Previous Score'
            congrats_message = f'{emoji.emojize(":trophy:", language="alias")} You have maintained the highest score in this category!'

    print(congrats_message)
    print(tabulate([score_table], headers=headers_value, tablefmt='grid', colalign=('center',)))
