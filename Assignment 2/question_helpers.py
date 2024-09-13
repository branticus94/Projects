# External imports
import random
import time
import html
from threading import Timer

# Imports from other modules I have written
from python_modules.api_helpers import get_categories_list
from python_modules.validation_helpers import get_integer
from python_modules.config import correct_celebrations, incorrect_letdowns, pre_selected_categories

# Colours
BRIGHT_CYAN = '\033[96m'
BRIGHT_YELLOW = '\033[93m'
YELLOW = '\033[33m'
WHITE = '\033[97m'
RED = '\033[91m'
GREEN = '\033[92m'
MAGENTA = '\033[95m'
RESET = '\033[97m'

global time_remaining

def generate_questions(questions, game_mode=None, game_round=None):
    # if a round is not specified we are in potluck mode therefore set question number to 0,
    # if in knockout mode multiply the round by 50 to get what question number we need to start on e.g. if the loop has
    # run once the round number would be one so question number is initialised at 50
    if game_round is not None:
        question_number = game_round * 50
    else:
        question_number = 0
        
    player_1_question_number = 1
    player_2_question_number = 1

    # create an empty list to store the question scores
    question_scores = []

    def time_up():
        global time_remaining
        time_remaining = False
        return

    global time_remaining
    time_remaining = True

    if game_mode == 'lightning':
        t = Timer(60, time_up)  # x is amount of time in seconds
        t.start()

    # Iterate over the dictionary of questions to display the question and answer, get user input and check if correct
    for i in questions:
        # Decodes html characters and initialises the variables question, correct answer and incorrect answer
        question = html.unescape(i["question"])
        correct_answer = html.unescape(i["correct_answer"])
        incorrect_answers = [html.unescape(ans) for ans in i["incorrect_answers"]]
        category = html.unescape(i["category"])

        # Initialises a list of total answers then shuffles the variables inside using the random library
        answers = incorrect_answers + [correct_answer]
        random.shuffle(answers)

        if not time_remaining:
            print(RED + "Time's up!" + RESET)
            break

        # Increment and print the question number:
        question_number += 1
        if game_mode == "pot_luck":
            category = f", category - {category}"
            print(MAGENTA + f"Question Number {question_number}{category}: " + RESET + f"\n\n{question}")
        elif game_mode == "head_to_head":
            if question_number % 2 == 0:
                print(BRIGHT_CYAN + "Player 2: ")
                print(MAGENTA + f"Question Number {player_2_question_number}: " + RESET + f"{question}")
                player_2_question_number += 1
            else:
                print(BRIGHT_CYAN + "Player 1: ")
                print(MAGENTA + f"Question Number {player_1_question_number}: " + RESET + f"{question}")
                player_1_question_number += 1

        else:
            print(MAGENTA + f"Question Number {question_number}: " + RESET + f"{question}")

        if game_mode != "lightning":
            time.sleep(0.5)

        if not time_remaining:
            print(RED + "Times up! This will be your last question, good luck!" + RESET)
            break
        # iterate over the answers list to display the answers to the user, if the answer is the correct answer
        # store this answer in the correct answer index variable
        j = 0
        correct_answer_index = 0
        for answer in answers:
            print(html.unescape(f"{j+1}.  {answer}"))
            if answer == correct_answer:
                correct_answer_index = j
            if game_mode != "lightning":
                time.sleep(1)
            j += 1
        print("")

        # Ask the user to make a guess
        user_guess = get_user_guess(answers)

        # compare user guess to answer using validate answer question and give a score,
        # if the question score is 0 and in knockout mode break out of the loop
        question_score = validate_answer(user_guess=user_guess, correct_answer_index=correct_answer_index, answers= answers, game_mode=game_mode)

        if question_score==0 and game_mode == 'knockout':
            break

        # Append the question score to the question scores list, this will be used to calculate the score for the round
        question_scores.append(question_score)

        if game_mode != "lightning":
            time.sleep(2)

    # Generate the round score by using the sum function on the question scores list
    if game_mode == "head_to_head":
        round_score = []
        player_1_score = sum(question_scores[i] for i in range(0, len(question_scores), 2))
        player_2_score = sum(question_scores[i] for i in range(1, len(question_scores), 2))
        round_score.append(player_1_score)
        round_score.append(player_2_score)
    else:
        round_score = sum(question_scores)

    # return the round score/round score list for multiplayer
    return round_score

def get_user_guess(answers):
    # use the get integer function to prompt the user for a guess and validate input
    user_guess = get_integer(BRIGHT_CYAN + "Please select the correct answer:\n" + RESET, 1, len(answers))
    time.sleep(1)
    # return the int of the user guess
    return user_guess

def validate_answer(user_guess, correct_answer_index, answers, game_mode=None):
    #  escape the html characters of the correct answer and store in variable called correct answer
    correct_answer = html.unescape(answers[correct_answer_index])

    # if the correct answer index is equal to the user guess (minus 1 to account for indexes starting at 0 print
    # that you are correct and set the score of the question to 1
    if correct_answer_index == (int(user_guess)-1):
        print(
            GREEN + f"\n{random.choice(correct_celebrations)}" + RESET + f" {correct_answer.replace(".", "")} is the correct answer \n")
        question_score = 1
        if game_mode != "lightning":
            time.sleep(0.5)
    # Otherwise print that the answer is incorrect and set the question score to 0
    else:
        print(
            RED + f"\n{random.choice(incorrect_letdowns)}" + RESET + f" {correct_answer.replace(".", "")} is the correct answer \n")
        if game_mode != "lightning":
            time.sleep(0.5)
        question_score = 0

    # return the question score
    return question_score

def display_score(score):
    # print current score
    print(YELLOW + f"Current score"+ RESET+f": {score}")
    time.sleep(1)

def print_all_categories():
    # run the get categories list to get all categories from trivia API
    categories = get_categories_list()["trivia_categories"]

    category_names = []

    for category in categories:
        category_names.append(category["name"])

    # Loop over the list of preselected categories, printing them and delay until print next
    for i in range (len(categories)):
        print(f"{i+1}. {category_names[i]}")
        time.sleep(0.25)

def select_a_category():
    # create a list of all the categories
    all_categories = (get_categories_list()['trivia_categories'])

    # Code to get a category, mode 10 lists all available categories in the API
    print("First lets " + BRIGHT_CYAN + "select a category" + RESET + ":")
    time.sleep(0.5)

    # Loop ove the list of preselected categories, printing them and delay until print next
    for i in range (len(pre_selected_categories)):
        print(f"{i+1}. {pre_selected_categories[i]}")
        time.sleep(0.25)

    time.sleep(2)

    # Get category from the user
    selected_category = get_integer("", 1, len(pre_selected_categories))

    # set a category id and name
    category_id = 0
    category_name = ""

    # If the user wants to see more than the preselected categories display them all and
    # set the category name and category id
    if selected_category == 10:

        # print message to the user to select an option
        print("\nWoah! Not enough options, well here you go!"+ BRIGHT_CYAN+ " Please select a category: " +RESET)

        # Call the print all categories function
        print_all_categories()

        # Get category from the user
        selected_category = get_integer("", 1, len(all_categories))

        # loop through the list of all categories if the category is equal to the selected category assign the
        # category id and category name
        for category in all_categories:
            if category == (all_categories[selected_category-1]):
                category_id = category['id']
                category_name = category['name']
    else:
        # iterate over the category names in all categories list, if the category name is equal to the
        # selected category set the category id and name
        for category in all_categories:
            if category['name'] == pre_selected_categories[selected_category - 1]:
                category_id = category['id']
                category_name = category['name']

    # return the category id and name
    return category_id, category_name