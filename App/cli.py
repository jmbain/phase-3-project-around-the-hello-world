import random
import time

def run():
    """This function runs the main game menu, which includes"""

    while True:
        prompt = """
        ~Around the Hello, World~
A python/basketball crossover (ha!) cli game

Around the Hello World is a game that tests your knowledge on python. 

Everytime you get an easy question right on the first try, you get TWO points!
Everytime you get a hard question right on the first try, you get THREE points!

If you get the question right on the second or third try, you will get partial points, depending on how easy or hard the question is.

Have fun and try to rack up points on the leaderboard!

Select an option:
1. Play the game
2. Peep the leaderboard
3. What's good with stats
4. Quit aka please no more puns
>> """
        option = input(prompt)
        if option == "1":
            play()
        elif option == "2":
            show_leaderboard()
        elif option == "3":
            show_advanced_stats()
        else: 
            print("This game broke my ankles")
            exit()

    

def play():
    """Runs when user selects Play Game from main game menu..."""
    pass

def attempt_and_score():
    """Runs when a user attempts a question, function also keeps track of number of attempts and score if correct/incorrect"""


def show_leaderboard():
    """Runs when user selects Leaderboard from main game menu..."""
    pass

def show_advanced_stats():
    """Runs when user selects advanced stats from main game menu..."""
    pass

def quit():
    """Runs when user selects quit from main game menu..."""
    pass


if __name__ == '__main__':
    run()