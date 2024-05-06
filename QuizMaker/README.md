# QUIZ MAKER
### Video Demo: https://youtu.be/Kfr809974ss
### Description:
This project is a Python based interactive Quiz Application which presents the users with 10 trivia questions from different categories and difficulty levels. Users then can select a category and difficulty level, answer the questions, and get scored out of 10 on their performance. Once the quiz is finished, the user can either quit or continue playing.

### Files:
#### project.py:
The 'project.py' file contains the implementation of the quiz application. It contains different methods each serve a different purpose. Below is the detailed explanation of each method.

* imports: Imports necessary libraries and modules such as BeautifulSoup for web scraping, pyfiglet for ASCII art, requests for making HTTP requests, and tabulate for displaying data in tabular format.

* main Function: The main() function controls the flow of the application by calling the functions in the order they need to be executed. It ensures that once the initial round of play is completed, a score board will be displayed and then the user will be presented with a choice to either continue or stop playing.

* print_message: This function displays the given string on the console in the form of selected ASCII art using 'PyFiglet' library. Here we are using this method to print 'Welcome' when the user starts the quiz and to print 'Goodbye' when the user stops playing.

* continue_playing: This function asks the user if they want to continue after playing atleast one round of quiz.

* fetch_all_categories: This function makes a call to Open Trivia Database API and uses web scraping to retrieve the list of categories.

* get_category and get_difficulty: These functions prompts the user to choose a category and required difficulty level.

* fetch_questions: This function retrives the questions from the Open Trivia Database API based on the category and difficulty level user selected.

* display_questions and display_question: These functions gets the list of questions, iterates through them and displays the questions and gets the answer from the user. It then checks if the user selected the correct option and updates the score accordingly. Once all the questions have been answered, then the total score will be displayed out of 10.

* get_user_answer: This function gets the answer from the user out of the given options.

#### display_scores.py:
This file focuses on managing and displaying scores. Here's what each part of the file does:

* imports: Imports necessary modules like csv, emoji, os, pyfiglet and tabulate.

* Score Management Functions: Contains functions like create_new_file, read_scores, update_scores, and display_score for creating a new CSV file for scores, reading existing scores, updating scores, and displaying the score leaderboard.

* display_score: This function displays the score in a visually appealing format using ASCII art and emojis, showcasing the user's current score, previous highest score (if any), and a congratulatory message if the user achieves a new high score.


#### test_project.py:
The 'test_project.py' contains functions to test the quiz application. Below is the detailed explanation of each method.

* test_fetch_all_categories: This function tests 'fetch_all_categories()' function from 'project.py' file. It verifies if the Open Trivia Database API is returning all the categories we are expecting.

* test_fetch_questions: This function 'tests fetch_questions()' function from 'project.py' file, ensuring the questions retrieved from API contains expected data.

* test_fetch_questions_difficulty: This function validates whether the retrieved questions match the specified difficulty level.

* test_fetch_questions_category: This function validates whether the retrieved questions match the specified category.

#### scores.csv:

* Score Tracking: The file allows the application to track and update the highest scores for each category as users play the game multiple times.

### Design Choices:
* API Usage: The application utilizes the **requests** library to interact with the Open Trivia Database API and retrieve necessary data.

* Beautiful Soup: For Webscraping, **Beautiful Soup** library is used to extract the list of categories from the website.

* User input Validation: Prompting the user again and again incase if the input entered is not valid. The user input is being handled by Try-except blocks wherever necessary.

* Display: In order to enhance user experience, various libraries are utilized to present visually appealing "Welcome", "Goodbye" and congratulations messages through the use of ASCII art, emojis, and tables.
