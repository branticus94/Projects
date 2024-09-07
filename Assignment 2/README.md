# Description
In this assignment I created a console app, written in python, which integrates with the superhero API and the Open Trivia Database. 

# Key features
The user first generates their quiz team name (key for any quiz related fun!) using the superhero API, they select a number which relates to a superhero ID and a power-stat to generate a username. I also save the output of an API request which relates to an image to a binary file to display to the user their character avatar using the pillow library with a mild insult to keep the game interesting! 

The app is a trivia app with three main game modes:
1. Pot luck - this has three rounds of 10 questions from any category within the API, the rounds get progressively more challenging starting with 'easy' mode through 'medium' and 'hard'. The score is then saved to the leaderboard csv.
2. Knockout mode - in this mode the user selects a category level and a difficulty level (easy, medium, difficult or all difficulties). More questions are provided until the user gets an incorrect answer and the game is over. The score is then saved to the leaderboard csv.
3. Multiplayer mode - two players go head to head with 10 general knowledge questions each. The scores are tallied and the winner is announced!

The user can also view the leaderboard from the main menu and see the top scores for pot luck and knockout mode. This is achieved by reading the csv to a pandas dataframe and manipulating the data to get a user friendly output which is then displayed in the console using the tabulate library.

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

# Ideas for future extension

It would be great to have a full blown GUI for the app!

Further logic I would like to add:
- Handling of HTTP error codes
- Ensuring the quiz team name generated is unique
- Further game modes e.g. timed mode/lighting round where the player answers as many questions as possible in a given time

**Many thanks for taking the time to review my code and providing feedback. Suggestions for improvements and/or enhancements are welcome!**

# How I used the APIs and how I installed external modules
I used two APIs for this project:
1. [Superhero API](c)
2. [Open Trivia Database](https://opentdb.com)

I used the superhero API to help generate a quiz team name by combining the name of a selected superhero (requesting the user to select a number between 1 and 731 - the maximum number of characters in the database) with the number score of the characters powerstat (out of 6 options). I also wrote the image of the hero to a binary file and displayed it to the user by employing the Image module of the Pillow/PIL library. 

I used the ```load_dotenv()``` function from the python-dotenv library to first load the environment variables stored in the .env file. I then used the ```getenv function``` of the built in python library os to get my superherokey saved in the .env file, I stored this in a variable named api_key. 

I then set the base url of the API request as 'https://superheroapi.com/api/' and added the access token followed by the selected id, performing two API requests using the ``.get()``` method of the requests library - one to get the image and one to get the powerstats. I used then used the ```.loads()``` method of the json libraray to convert to json for easy manipulation and saved the data into a variable.

The second API, the open trivia database, did not require a key generated with github. In order to use the database I created a get session token function which  
called the API endpoint which allows you to retrieve a session token 'https://opentdb.com/api_token.php?command=request', again this used the ```.get()``` method of the requests library to retrieve the data which was then converted to json format for manipulation. 

This token is called upon opening the app and it allows you to not see the same questions twice. As one could exhaust all the possible questions I also created a reset session token function which hits this API endpoint 'https://opentdb.com/api_token.php?command=reset&token=YOURTOKENHERE' and is called if response code 4 is sent back by the API. I dynamically created different API requests based on user selection of game mode. The API requests looked like this, obviously the parameter values changed depending on game mode: ```https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple```. Again using the get method to retrieve the data and loads method to convert to json. I also hit their other API endpoints - category lookup and category question count lookup so that I could run knockout mode accordingly.

In order to make the app run I relied on a host of built in and external imports. 

I utilised the built in imports such as random, time, datetime, os and csv by adding a list of imports at the top of the file with ```import import_name```:
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

As mentioned above, I created a requirements.txt file using the ```pip freeze``` command to allow others to setup their environment in a similar manner and install the necessary packages (of the specified version) to their machine in the project file. 
