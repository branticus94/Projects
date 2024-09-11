import pyfiglet
import time

BRIGHT_YELLOW = '\033[93m'
YELLOW = '\033[33m'
WHITE = '\033[97m'
RED = '\033[91m'
BRIGHT_CYAN = '\033[96m'
GREEN = '\033[92m'
MAGENTA = '\033[95m'
RESET = '\033[97m' # called to return to standard terminal text color

def print_game_over():
    print("\nSkipping the new game, huh? Guess you’re saving your energy for\nsomething more exciting — like maybe a nap?\n")
    time.sleep(1)
    game_over = pyfiglet.figlet_format(" Game Over! ")
    print(RED + game_over + RESET,end="")

def print_final_score(score):
    time.sleep(1)
    final_score = pyfiglet.figlet_format(f"       Final Score: {score}    ")
    print(BRIGHT_CYAN + final_score + RESET,end="")

def print_title():
    title = pyfiglet.figlet_format("? ?   Quiz Py   ? ?")
    print(BRIGHT_YELLOW + title + RESET, end="")

def print_game_mode(game_mode):
    game_mode = pyfiglet.figlet_format(f"         {game_mode}      ")
    print(GREEN + game_mode + RESET, end="")

def print_leaderboard():
    leaderboard = pyfiglet.figlet_format("Leaderboard")
    print(GREEN + leaderboard + RESET, end="")

def print_banner():
    hard_return = "-------------------------------------------------------------"
    star_banner = "#############################################################"

    print(YELLOW + hard_return + RESET)
    print(WHITE + star_banner + RESET)
    print(YELLOW + hard_return + RESET)

def print_round_number(i, difficulty):
    round_logo = pyfiglet.figlet_format(f"          Round {i}          ")

    print(BRIGHT_CYAN + round_logo + RESET, end="")
    print(BRIGHT_CYAN + f"                Difficulty level: {difficulty.title()}\n" + RESET)
    time.sleep(1)

def print_title_card():
    print_banner()
    time.sleep(1)
    print_title()
    time.sleep(1)
    print_banner()
    time.sleep(1)

def print_menu():
    menu = pyfiglet.figlet_format(f"                Menu          ")
    print(MAGENTA + menu + RESET, end="")

def print_winning_player(player_number):
    if type(player_number) is int:
        player_number = pyfiglet.figlet_format(f"   Player {player_number} wins!         ")
    else:
        player_number = pyfiglet.figlet_format(f"   It's a draw!         ")
    print(GREEN + player_number + RESET)
    time.sleep(1)