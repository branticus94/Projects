# Built in imports
import json
import random
import time
import datetime
import os
import csv

# External imports
from playsound import playsound
import pandas as pd
from PIL import Image
from tabulate import tabulate
from dotenv import load_dotenv
import requests as req
from pathlib import Path

# Imports from modules I have created within the project
from python_modules.api_helpers import get_session_token, get_category_question_count, generate_api_request_url, get_api_data, generate_api_request_method_2
from python_modules.validation_helpers import get_integer, get_yes_no
from question_helpers import generate_questions, select_a_category, display_score
from python_modules.graphics_helpers import print_banner, print_game_over, print_title_card, print_round_number, \
    print_game_mode, print_winning_player, print_menu, print_leaderboard, print_final_score
from python_modules.config import psych_up_comments, appearance_comments, agree_responses, easy_mode_comments, medium_mode_comments, \
    hard_mode_comments, all_difficulties_comments, leaderboard_comments

BRIGHT_CYAN = '\033[96m'
BRIGHT_YELLOW = '\033[93m'
YELLOW = '\033[33m'
WHITE = '\033[97m'
RED = '\033[91m'
GREEN = '\033[92m'
MAGENTA = '\033[95m'
RESET = '\033[97m'

def confirm_play_game():

    # Prompt user to confirm if they wish to play a game
    print(WHITE + "  Welcome to QuizPy! A console trivia app written in python  \n")
    time.sleep(1)

    # Use the get yes or no function I created in the validation helpers module to get a y or n entry with error handling
    response = get_yes_no("              Do you want to play a game? (y/n)              \n")
    time.sleep(1)

    # if the user decides not to play print the game over graphic and failure trumpet noise
    if response == "n":
        print_game_over()
        playsound("assets/fail-muted-trumpet.wav")
        quit()
    else:
        # Print the banner and menu graphic
        print_banner()
        time.sleep(1)
        print(WHITE + random.choice(agree_responses))
        time.sleep(1)

def prompt_menu_options():
    # Print the menu
    print("Please select an " + BRIGHT_CYAN + "option" + RESET + " from the menu below:")
    time.sleep(1)
    print(RED + "1. Pot Luck")
    time.sleep(1)
    print(BRIGHT_YELLOW +"2. Knockout")
    time.sleep(1)
    print(WHITE + "3. Head-to-Head")
    time.sleep(1)
    print(GREEN + "4. Lightening")
    time.sleep(1)
    print(BRIGHT_CYAN +"5. View Leaderboard")
    time.sleep(1)
    print(MAGENTA + "6. Exit Game\n"+ RESET)
    time.sleep(1)

    # Use the get integer function I defined in the validation errors module to get a valid integer input from 1 to 6
    game_mode = get_integer("Enter your choice:\n", 1, 6)

    # Print the banner
    time.sleep(2)
    print("")
    print_banner()
    time.sleep(2)

    # return which game mode the user has selected
    return game_mode

def generate_quiz_name():
    # Load environment variables where the api key is held
    load_dotenv()

    # Get the API key from the .env file
    api_key = os.getenv('SUPERHERO_API_KEY')

    # Set the base url of the api request which the parameters will be added to
    base_url = "https://superheroapi.com/api/"

    # There are 731 superheros in the API therefore to generate the name I ask the user to select a number between
    # 1 and 731 using the get integer function I defined in the get integer module
    superhero_name_id = get_integer("\nFirst lets generate your "+GREEN +"quiz team name"+ RESET+
                                    "! Pick a number between 1 and 731:\n", 1, 731)

    # Prompt the user to enter one of the 6 characteristics in the power stats of characters held on the API
    time.sleep(1)
    print("\nExcellent choice! Now, please select a " + BRIGHT_CYAN +"characteristic" +RESET +" (1-6):")
    time.sleep(1)
    print(RED + "1. Intelligence",end='')
    time.sleep(0.5)
    print(BRIGHT_YELLOW + "\n2. Strength",end='')
    time.sleep(0.5)
    print(MAGENTA + "\n3. Speed",end='')
    time.sleep(0.5)
    print(BRIGHT_CYAN + "\n4. Durability",end='')
    time.sleep(0.5)
    print(WHITE + "\n5. Power",end='')
    time.sleep(0.5)
    print(GREEN + "\n6. Combat\n" + RESET,end='')
    time.sleep(0.5)
    superhero_power_stat_id = get_integer("",1,6)

    # Use an if/else statement to set the superhero power stat based on the input integer
    if superhero_power_stat_id == "1":
        superhero_power_stat = "intelligence"
    elif superhero_power_stat_id == "2":
        superhero_power_stat = "strength"
    elif superhero_power_stat_id == "3":
        superhero_power_stat = "speed"
    elif superhero_power_stat_id == "4":
        superhero_power_stat = "durability"
    elif superhero_power_stat_id == "5":
        superhero_power_stat = "power"
    else:
        superhero_power_stat = "combat"

    # Hit the superhero API twice using the get function of the requests HTTP library imported
    # to get the power stats of the selected superhero and the image request
    api_request_power_stats = req.get((base_url + api_key + f"/{superhero_name_id}/powerstats"))
    api_request_image = req.get((base_url+api_key+f"/{superhero_name_id}/image"))

    # Use the built-in python package json to load the data for the power stats and the image data
    api_request_power_stats_json = json.loads(api_request_power_stats.text)
    api_request_image_json = json.loads(api_request_image.text)

    # Get the superhero name, power stat and image url from the loaded data
    name = api_request_image_json['name']
    image_url = api_request_image_json['url']
    power_stat = api_request_power_stats_json[superhero_power_stat]

    # Sometimes the power stat is null I handle this by using the inbuilt random module
    # in python and the randint method to generate a number between 1 and 100
    if power_stat == "null":
        power_stat = str(random.randint(1,100))

    # Combine the name and the power stat and join them using underscores
    quiz_name = name + "_" + power_stat
    updated_quiz_name = quiz_name.replace(" ", "_")

    # Print a friendly console message
    print(f"Hey "+MAGENTA+f"{updated_quiz_name}"+ RESET + f", {random.choice(psych_up_comments)}\n")
    time.sleep(1)

    # Set the file path I am going to save the image to
    file_path_image = "assets/downloaded_image.jpg"

    # Get the image from the image url
    response = req.get(image_url)

    # Ensure the request was successful (status code 200)
    if response.status_code == 200:

        # Open the file in binary write mode and save the content
        with open(file_path_image, "wb") as file:
            file.write(response.content)

        # Load and display image
        player_image = Image.open('assets/downloaded_image.jpg')

        # Print a random comment, mildly insulting the appearance of the character
        print(f"{random.choice(appearance_comments)}")
        time.sleep(1)

        # show the players image
        player_image.show()

    print("\nOn with the quiz!")
    time.sleep(5)

    # Return the quiz name so that we can add it to the leaderboard later
    return updated_quiz_name

def run_pot_luck_mode():
    # Pot luck mode will take the user through three rounds of 10 questions,
    # Each round of question will escalate in difficult: easy, medium and then hard

    global quiz_team_name, token

    # Print the graphic to the user with round name using the print game mode function
    # defined in the graphic helpers module
    print_game_mode("Pot Luck")
    time.sleep(0.5)

    # Print information to the user about how the mode works
    print("Welcome to Pot Luck mode, here you will be presented with 10 trivia ")
    print("questions from a random category. There are three rounds which get ")
    print("progressively more difficult.\n")
    time.sleep(4)

    # Initialise a list of difficulty levels and a string variable which
    # holds the type of questions we are requesting from the API (multiple choice)
    difficulty_levels = ['easy', 'medium', 'hard']
    question_type="multiple"

    # Set the round to 1 and initialise an empty list to hold all the round scores
    i = 1
    round_scores = []

    # Iterate over the difficulty levels to generate an API request, display questions and answers,
    # get user input and validate if correct, updating the score:
    for difficulty_level in difficulty_levels:

        # Print the round number
        print_round_number(i, difficulty_level)

        # generate an API request url for 10 questions of any category at the current difficulty level
        # with the question type and session token provided
        request_url = generate_api_request_url(10,None, difficulty_level, question_type, token)

        # use thee get api data function from api helpers module to retrieve data from the url
        questions_request_results = get_api_data(request_url, token)

        # play the game and assign the returned score to a round score variable
        round_score = generate_questions(questions_request_results, game_mode="pot_luck")

        # Append the score to the round scores list
        round_scores.append(round_score)

        # Print the running total to the user by summing the round_scores list
        total_score = sum(round_scores)

        # Print out the total score to the user
        display_score(total_score)
        time.sleep(2)

        # Increment 'i' used to print the round number
        i += 1

    final_score = sum(round_scores)

    # Print the final score
    print_final_score(final_score)

    # Get the current time using the now method of the datetime class in the datetime module
    current_time = datetime.datetime.now()

    # use the save_to_leaderboard_csv function defined in the csv_helpers
    # module to save the total score to the leaderboard
    save_to_leaderboard_csv(score=final_score, date_time=current_time, game_mode="Pot Luck")

    # see if the user wishes to play another game
    play_again()

def run_knockout_mode():
    # Knockout mode will allow the user to select a category of their choice,
    # a difficulty level, they will continue to receive questions until they get a wrong answer
    global quiz_team_name, token

    # # As the session token is used to track questions I reset this incase an alternate mode has been played
    # # prior and there are too few questions left
    # session_token = reset_session_token(session_token)['token']

    difficulty_levels = ['easy', 'medium', 'hard', 'all']
    question_type = None

    # Call the print game mode function to print the logo
    print_game_mode("Knockout")

    time.sleep(0.5)

    # Print information on the console to describe how game mode is selected
    print("Welcome to Knockout Mode! Choose a category and difficulty level.")
    print("Keep answering questions correctly to stay in the game. One wrong")
    print("answer, and you're out!\n")

    time.sleep(3)

    # Call the select a category function
    category_id, category_name = select_a_category()

    time.sleep(1)

    # Get difficulty mode using the get integer function defined in the validation helpers module
    print(f"\nYou selected " +BRIGHT_CYAN + f"{category_name.lower()} "+ RESET + f"- great choice! Now lets select a "+ MAGENTA + "difficulty level:" + RESET)
    i = 1
    for difficulty in difficulty_levels:
        time.sleep(0.25)
        print(f"{i}. {difficulty.title()}")
        i += 1
    time.sleep(1)
    selected_difficulty_int = get_integer("", 1, len(difficulty_levels))
    time.sleep(1)

    # use a variable to store the selected difficulty level
    selected_difficulty_level = difficulty_levels[selected_difficulty_int-1]

    # get number of questions in category using the get category question count
    # method providing the selected category id
    category_question_count = get_category_question_count(category_id)

    # Depending on the difficulty level selected print a comment on the level, set the total questions based on the
    # item in the dictionary of data generated which stores the question count for the specific category selected
    if selected_difficulty_level=='easy':
        print(f"\n{random.choice(easy_mode_comments)}\n")
        total_questions = category_question_count['category_question_count']['total_easy_question_count']
    elif selected_difficulty_level=='medium':
        print(f"\n{random.choice(medium_mode_comments)}\n")
        total_questions = category_question_count['category_question_count']['total_medium_question_count']
    elif selected_difficulty_level=='hard':
        print(f"\n{random.choice(hard_mode_comments)}\n")
        total_questions = category_question_count['category_question_count']['total_hard_question_count']
    else:
        print(f"\n{random.choice(all_difficulties_comments)}\n")
        selected_difficulty_level = None
        total_questions = category_question_count['category_question_count']['total_question_count']

    # API can only accept 50 requests at a time, this handles the error by only requesting
    # the total amount of questions if there are less than 50
    remaining_questions = total_questions
    round_scores = []

    # while there are more questions remaining I will loop over the below to generate questions, if there are more than
    # 50 questions I request the maximum amount from the API otherwise I request the specified amount
    while remaining_questions > 0:
        # setting the round number at 0, this is used when calculating the question number to display to the user
        round_number = 0

        # if there are less than 50 questions remaining I set the amount of questions I want to request to the
        # remaining questions and reset the remaining questions otherwise I set it to 50 (maximum for API) and
        # reduce the amount of remaining questions accordingly
        if remaining_questions < 50:
            amount = remaining_questions
            remaining_questions = 0
        else:
            amount = 50
            remaining_questions = total_questions - amount

        # Use the generate api request url function from the api helpers module to hit the API with the specified
        # parameters
        request_url = generate_api_request_url(amount=amount, category=category_id, difficulty=selected_difficulty_level, question_type=question_type, token=token)

        # use the get_api_data function to get question data
        question_request_results = get_api_data(request_url, token)

        # use the generate questions function in the question helpers module to run for a round save the
        # returned round score in a variable round score
        round_score = generate_questions(question_request_results, game_mode="knockout", game_round=round_number)

        # appends the round score to the list of round scores
        round_scores.append(round_score)

        # if the round score is less than the amount of questions then the player must have been knocked
        # out so exit the while loop
        if round_score < amount:
            break

        # increment the round number
        round_number += 1

    # calculate the total score using the sum function on the round scores list
    total_score = sum(round_scores)

    # print the output of the total scores to the user
    print_final_score(total_score)

    # get the current time so that it can be added to the leaderboard
    current_time = datetime.datetime.now()

    # Use the save to leaderboard csv function to save the output to the leaderboard
    save_to_leaderboard_csv(score=total_score, date_time=current_time, game_mode="Knockout")

    # see if user wants to play again
    play_again()


def run_head_to_head_mode():
    # Multiplayer mode will allow two players to play against one another
    # in the general knowledge category, there will be 10 questions each of a random
    # difficulty and the function will
    global token

    # Call print game mode function defined in graphics helpers module to display game mode and delay
    print_game_mode("Head to Head")
    time.sleep(1)

    # Print message to the user explaining how head-to-head mode works
    print("Welcome to Head to Head! Challenge another player in a fun, one-on-one match. You will gt 10 general "
          "\nknowledge questions each. It’s all about friendly competition, so jump in, enjoy the game, "
          "\nand may the best player win! \n")
    time.sleep(5)

    # Generate API request url for 20 multiple choice general knowledge questions of any difficulty
    api_request_url = generate_api_request_url(20, 9, difficulty=None, question_type='multiple', token=token)

    # Get the question and answer data
    question_data = get_api_data(api_request_url, token)

    # Fun the generate questions function to enter the head-to-head game mode
    scores = generate_questions(question_data, game_mode="head_to_head")

    # Retrieve the scores from the list and assign to player 1/2 accordingly
    player_1_score = scores[0]
    player_2_score = scores[1]

    # print final scores
    print("After a fierce battle, sweat, and maybe a little bit of luck, the final scores have been tallied. "
          "Drumroll please...\n")
    playsound("assets/drum_roll.wav")
    print(MAGENTA + "Player 1: " + RESET + f"{player_1_score}")
    time.sleep(1)
    print(BRIGHT_CYAN + "Player 2: " + RESET + f"{player_2_score}")
    time.sleep(3)

    # Check which player wins and display message to screen
    if player_1_score > player_2_score:
        print_winning_player(1)
    elif player_1_score < player_2_score:
        print_winning_player(2)
    else:
        print_winning_player("draw")

    # see if the user wishes to play another game
    play_again()

def run_lightning_round():

    lightening_categories = [
        {"name": "General Knowledge", "id": 9},
        {"name": "Entertainment: Books", "id": 10},
        {"name": "Entertainment: Film", "id": 11},
        {"name": "Entertainment: Music", "id": 12},
        {"name": "Entertainment: Television", "id": 10},
        {"name": "Science & Nature", "id": 17},
    ]

    print_game_mode("Lightning")

    print("\nWelcome to Lightning Round! With 60 seconds on the clock how many questions can you correctly answer?\n")

    print("Please choose a "+ BRIGHT_CYAN + "category:"+RESET)
    for index, value in enumerate (lightening_categories, start=0):
        print(f"{index+1}. {value['name']}")

    print("")

    category_number = get_integer("",1, len(lightening_categories))
    selected_category = lightening_categories[category_number-1]["id"]

    question_data = generate_api_request_method_2(amount=50, category=selected_category, token=token)

    print("")

    final_score = generate_questions(question_data, game_mode="lightening")

    # print the output of the total scores to the user
    print_final_score(final_score)

    # get the current time so that it can be added to the leaderboard
    current_time = datetime.datetime.now()

    # Use the save to leaderboard csv function to save the output to the leaderboard
    save_to_leaderboard_csv(score=final_score, date_time=current_time, game_mode="Lightening")

    # see if user wants to play again
    play_again()


def generate_leaderboard():
    # List to store game modes
    game_modes = ['Knockout', 'Pot Luck', 'Lightening']

    # Print the tittle of mode and delay
    print_leaderboard()
    time.sleep(2)

    # Print a random comment about scores and delay
    print(f"{random.choice(leaderboard_comments)}\n")
    time.sleep(2)

    # Prompt for a game mode selection
    print(f"Please select a "+ MAGENTA + "game mode" + RESET +" to view the scores!:")
    time.sleep(1)

    # Display game modes
    for i, game_mode in enumerate (game_modes, 1):
        print(f"{i}. {game_mode}")

    # Get user selection
    selected_game_mode_index = get_integer("", 1, len(game_modes))
    game_mode = game_modes[selected_game_mode_index-1]
    time.sleep(2)

    # Print the game mode selection to the user
    print(f"\nDrums please! The winners for "+BRIGHT_CYAN + f"{game_mode} " + RESET + f"are:\n")

    # Play a drum roll
    playsound("assets/drum_roll.wav")

    try:
        # Read the csv into a pandas dataframe
        leaderboard = pd.read_csv('leaderboard.csv')

        # Convert the date column to datetime format
        leaderboard['datetime'] = pd.to_datetime(leaderboard['datetime'])

        # Change the datetime format and add a new column, date_formatted
        leaderboard['date_formatted'] = leaderboard['datetime'].dt.strftime('%Y/%m/%d')

        # Drop the datetime column from the dataframe
        leaderboard_remove_datetime = leaderboard.drop(columns='datetime')

        # filter the leaderboard by game mode
        filtered_leaderboard = leaderboard_remove_datetime[leaderboard_remove_datetime['mode'] == game_mode]

        # Change datatype of score to int
        filtered_leaderboard.loc[:, 'score'] = pd.to_numeric(filtered_leaderboard['score'])

        # sort the filtered leaderboard by descending score
        sorted_filtered_leaderboard = filtered_leaderboard.sort_values(by='score', ascending=False,ignore_index=True)

        # Rename the columns from the csv
        sorted_filtered_leaderboard_renamed = sorted_filtered_leaderboard.rename(columns = {'quiz_name': 'Quiz Team Name', 'score': 'Score', 'mode': 'Mode', 'date_formatted':'Date'})

        # Format for center alignment in tabulate
        col_align = ["center", "center", "center", "center"]

        # use the tabulate function imported from the tabulate library, allowing me to format the dataframe in an
        # aesthetically pleasing format and print output
        print(tabulate(sorted_filtered_leaderboard_renamed, headers='keys', tablefmt='psql', showindex=False, colalign=col_align))

    except FileNotFoundError:
        print(RED + "Looks like the leaderboard is empty - get playing!" + RESET)

    # see if user wants to play again
    play_again()

def save_to_leaderboard_csv(score, date_time, game_mode):
    global quiz_team_name

    # create a variable file to store the path to the leaderboard file
    file = Path('leaderboard.csv')

    if not file.is_file():
        with open(file, 'w', newline='') as csvfile:
            # Create a csv.writer object
            writer = csv.writer(csvfile)

            # Define the header row
            header = ['quiz_name', 'score', 'mode', 'datetime']

            # Write the header row to the CSV file
            writer.writerow(header)

    # Create a new row list which holds the quiz name, score, date_time and game mode for saving
    # (the arguments passed in with the function)
    new_row = [quiz_team_name, score, game_mode, date_time]

    # use the csv writer to add a row
    with open(file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_row)

def select_and_run_game_mode():
    global quiz_team_name, token
    # print the menu logo
    print_menu()
    time.sleep(2)

    # Run the prompt menu options function which returns the int of the option that the user has chosen
    game_choice = prompt_menu_options()

    # Use if function to run the different modes based on the outcome of the menu
    if game_choice == 1:
        run_pot_luck_mode()
    elif game_choice == 2:
        run_knockout_mode()
    elif game_choice == 3:
        run_head_to_head_mode()
    elif game_choice == 4:
        run_lightning_round()
    elif game_choice == 5:
        generate_leaderboard()
    else:
        print_game_over()
        playsound("assets/fail-muted-trumpet.wav")
        time.sleep(5)
        quit()

def play_again():
        global quiz_team_name, token

        play_again_response = get_yes_no("\nWould you like to return to the " + BRIGHT_YELLOW + "main menu" + RESET + "? (y/n)\n")
        time.sleep(1)

        if play_again_response == "y":
            time.sleep(1)
            print("\nExcellent on with the game!\n")
            time.sleep(2)
            print_banner()
            time.sleep(2)
            select_and_run_game_mode()
        else:
            print_game_over()
            playsound("assets/fail-muted-trumpet.wav")
            quit()

# At the startup of the app get a session token using the get session token
token = get_session_token()['token']

# play the entry music using the playsound function of the playsound library
# playsound("assets/trivia_game_entry.wav")

# print the title card
# print_title_card()

# run the confirm play game function to ensure the user wishes to play otherwise - game over
confirm_play_game()

# Generate a quiz team name using the generate quiz name function, storing the return value
# in the quiz team name variable (used for the leaderboard)
quiz_team_name = generate_quiz_name()

# print the banner for graphical interest
print_banner()

# run the menu and game mode
select_and_run_game_mode()