from project import fetch_all_categories
from project import fetch_questions
import time


def test_fetch_all_categories():
    categories_list = ['Any Category', 'General Knowledge', 'Entertainment: Books', 'Entertainment: Film', 'Entertainment: Music',
                       'Entertainment: Musicals & Theatres', 'Entertainment: Television', 'Entertainment: Video Games', 'Entertainment: Board Games',
                       'Science & Nature', 'Science: Computers', 'Science: Mathematics', 'Mythology', 'Sports', 'Geography', 'History', 'Politics', 'Art',
                       'Celebrities', 'Animals', 'Vehicles', 'Entertainment: Comics', 'Science: Gadgets', 'Entertainment: Japanese Anime & Manga',
                       'Entertainment: Cartoon & Animations']
    categories = fetch_all_categories()
    assert len(categories) == 25
    for category in list(categories.keys()):
        assert category in categories_list


def test_fetch_questions():
    questions = fetch_questions('any', 'any')
    questions_keys = list(questions[5].keys())
    assert 'type' in questions_keys
    assert 'difficulty' in questions_keys
    assert 'category' in questions_keys
    assert 'question' in questions_keys
    assert 'correct_answer' in questions_keys
    assert 'incorrect_answers' in questions_keys
    time.sleep(5)


def test_fetch_questions_difficulty():
    difficulty_level = 'easy'
    questions = fetch_questions('any', difficulty_level)
    for question in questions:
        assert question['difficulty'] == difficulty_level
    time.sleep(5)


def test_fetch_questions_category():
    category = 'Sports'
    category_index = fetch_all_categories()[category]
    questions = fetch_questions(category_index, 'any')
    for question in questions:
        assert question['category'] == category
    time.sleep(5)
