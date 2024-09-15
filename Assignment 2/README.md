# Contents
- [Description](#description)
- [Key Features](#key-features)
- [What is in the file](#what-is-in-the-file)
- [What you will need to set up the file](#what-you-will-need-to-set-up-the-file)
- [Ideas for Future Extension](#ideas-for-future-extension)
- [How I used APIs](#how-i-used-apis)
- [How I used and installed external modules](#how-i-used-and-installed-external-modules)
- [Gameplay Video](#gameplay-video)

# Description
In this assignment I created a console app, written in python, which integrates with the superhero API and the Open Trivia Database. 

# Key features
The user first generates their quiz team name (key for any quiz related fun!) using the superhero API, they select a number which relates to a superhero ID and a power-stat to generate a username. I also save the output of an API request which relates to an image to a binary file to display to the user their character avatar using the pillow library with a mild insult to keep the game interesting! 

The app is a trivia app with three main game modes:
1. Pot luck - this has three rounds of 10 questions from any category within the API, the rounds get progressively more challenging starting with 'easy' mode through 'medium' and 'hard'. The score is then saved to the leaderboard csv.
2. Knockout mode - in this mode the user selects a category level and a difficulty level (easy, medium, difficult or all difficulties). More questions are provided until the user gets an incorrect answer and the game is over. The score is then saved to the leaderboard csv.
3. Multiplayer mode - two players go head to head with 10 general knowledge questions each. The scores are tallied and the winner is announced!

The user can also view the leaderboard from the main menu and see the top scores for pot luck and knockout mode. This is achieved by reading the csv to a pandas dataframe and manipulating the data to get a user-friendly output which is then displayed in the console using the tabulate library.

# What is in the file
The file structure contains:
- The main python file QuizPy with the main game logic 
- A .gitignore file so that my API key for the superhero database is not shared
- A directory containing the assets where some sound effects are stored and the image the user generates is stored in binary mode to a jpeg file. 
- A leaderboard csv where the results of the knockout mode and potluck mode are stored
- A directory containing several modules I have written with various functions relating to:
    - functions to perform API request and handle error codes
    - functions which generate ASCII art for the various modes to add some visual appeal
    - validation functions to help validate if the input is an int within a defined limit or if the input is y/n
    - functions which display the question to the user and get a score
- A requirements file so that others can install the necessary modules and emulate my environment

# What you will need to set up the file
1. Ensure that you have the necessary requirements installed 
This can be done using the following pip command
```
pip install -r requirements.txt
```
2. Create a .env file to store your Superhero API key in the root directory (files with the .env extension are included in the .gitignore file to maintain safety of the API key):
<img width="407" alt="image" src="https://github.com/user-attachments/assets/5d04f34c-2f8c-4f76-b44a-7be171868f93">

3. Visit the [superhero API](https://superheroapi.com) and generate an API key by signing in with your GitHub account:
<img width="452" alt="image" src="https://github.com/user-attachments/assets/0adcfb63-820e-4f92-93e1-a1a8cbcdc00b">

4. Add the API key to your .env file in the format:
```
SUPERHERO_API_KEY=your_api_key_here
```
You should be good to go!

5. NB[^1]: When installing the playsound library I encountered an error which stated that my wheel was outdated, after a few hours of playing around with fixes recommended online I found out that if you update the wheel using ``` pip install --upgrade pip setuptools wheel ``` all is well, Woo-hoo! Just sharing the love incase you encounter this error too! You could always comment out the playsound module import on line 10 of quizpy.py and comment out the calls to playsound which are located at line 48, 414, 528, 547 and 554 in the quizpy.py file - although you will miss out on comical gameplay music!
   
[^1]: For the longest time I thought NB stood for "note before" however is actually from the latin "nota bene" - note well, thought this was 

# Ideas for future extension

It would be great to have a full-blown GUI for the app!

Further logic I would like to add:
- Handling of HTTP error codes
- Ensuring the quiz team name generated is unique
- Further game modes e.g. timed mode/lighting round where the player answers as many questions as possible in a given time

**Many thanks for taking the time to review my code and providing feedback. Suggestions for improvements and/or enhancements are welcome!**

# How I used APIs
I used two APIs for this project:
1. [Superhero API](http://superheroapi.com)
2. [Open Trivia Database](https://opentdb.com)

I used the superhero API to help generate a quiz team name by combining the name of a selected superhero (requesting the user to select a number between 1 and 731 - the maximum number of characters in the database) with the number score of the characters power-stat (out of 6 options). I also wrote the image of the hero to a binary file and displayed it to the user by employing the Image module of the Pillow/PIL library. 

I used the ```load_dotenv()``` function from the python-dotenv library to first load the environment variables stored in the .env file. I then used the ```getenv function``` of the built-in python library os to get my superhero key saved in the .env file, I stored this in a variable named api_key. 

I then set the base url of the API request as 'https://superheroapi.com/api/' and added the access token followed by the selected id, performing two API requests using the ```.get()``` method of the requests library - one to get the image and one to get the power-stats. I used then used the ```.loads()``` method of the json library to convert to json for easy manipulation and saved the data into a variable.

The second API, the open trivia database, did not require a key generated with gitHub. In order to use the database I created a get session token function which  
called the API endpoint which allows you to retrieve a session token 'https://opentdb.com/api_token.php?command=request', again this used the ```.get()``` method of the requests library to retrieve the data which was then converted to json format for manipulation. 

This token is called upon opening the app, and it allows you to not see the same questions twice. As one could exhaust all the possible questions I also created a reset session token function which hits this API endpoint 'https://opentdb.com/api_token.php?command=reset&token=YOURTOKENHERE' and is called if response code 4 is sent back by the API. I dynamically created different API requests based on user selection of game mode. The API requests looked like this, obviously the parameter values changed depending on game mode: ```https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple```. Again using the get method to retrieve the data and loads method to convert to json. I also hit their other API endpoints - category lookup and category question count lookup so that I could run knockout mode accordingly.

# How I used and installed external modules
In order to make the app run I relied on a host of built-in and external imports. 

I utilised the built-in imports such as random, time, datetime, os and csv by adding a list of imports at the top of the file with ```import import_name```:
```
# Built in imports
import json
import random
import time
import datetime
import os
import csv
```
I then also used several external libraries. In order to use them I first needed to navigate to the terminal to install the packages within my project file. 

In order to do this I used the pip (python install package manager) command ```pip install package_name``` to install the package. 

Once installed, I used import statement at the top of my file again to import the whole library or a particular module as below:
```
# External imports
from playsound import playsound
import pandas as pd
from PIL import Image
from tabulate import tabulate
from dotenv import load_dotenv
import requests as req
```

As mentioned above, I created a requirements.txt file using: ```pip freeze > requirements.txt``` command to allow others to set up their environment in a similar manner and install the necessary packages (of the specified version) to their machine in the project file. 

# Gameplay video

## Contents
- [Opening Menu and Generate Quiz Name](#opening-menu-and-generate-quiz-name)
- [Potluck](#potluck)
- [Knockout](#knockout)
- [Head to Head](#head-to-head)
- [Leaderboard](#leaderboard)
- [Exit](#exit)

### Opening menu and generate quiz name
The opening menu allows you to set up and start a trivia session. A quiz team name is generated, which helps identify your game in the leaderboard and adds a fun, personalized touch before the trivia begins.
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/2edApUOy0BI/0.jpg)](https://www.youtube.com/watch?v=2edApUOy0BI)

### Potluck
In the Potluck mode, questions come from a random assortment of categories. There are 3 rounds of 10 questions. The difficulty increases with each round
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/yPhNEKsoONU/0.jpg)](https://www.youtube.com/watch?v=yPhNEKsoONU)

### Knockout
Knockout mode is an elimination-style game. Players compete to stay in the game by answering correctly, and a wrong answer knocks them out of the competition.
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/S4fmLuaaWh0/0.jpg)](https://www.youtube.com/watch?v=S4fmLuaaWh0)

### Head to head
In this mode, two players or teams face off against each other in direct competition. They take turns answering questions, and the player or team with the most correct answers wins. There are 10 questions each of a random category/difficulty level.
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/5WPRwBpCk4A/0.jpg)](https://www.youtube.com/watch?v=5WPRwBpCk4A)

### Lightning 
In this mode, players have 60 seconds to answer as many questions they can from a limited list of categories.
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Ds7p49i1up0/0.jpg)](https://www.youtube.com/watch?v=Ds7p49i1up0)

### Leaderboard
The leaderboard mode allows you to see the leaderboard for potluck or knockout mode. Before the scores are released a drum roll plays for added fun!
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Tpp4cp-qLy8/0.jpg)](https://www.youtube.com/watch?v=Tpp4cp-qLy8)

### Pub Quiz Generator
The pub quiz generator prompts the user to select 5 unique categories and generates a text file quiz for use in home pub quiz games!
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/fzq7OM2ijS0/0.jpg)](https://www.youtube.com/watch?v=fzq7OM2ijS0)

### Exit
At the end of the game a fun "Wamp Wamp Wamp Waaaaaaaamp" style sound plays and the application ends
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/6GSYO1VsLVU/0.jpg)](https://www.youtube.com/watch?v=6GSYO1VsLVU)
