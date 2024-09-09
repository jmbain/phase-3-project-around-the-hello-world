import random
import sqlite3

# Creates connection to scores database
conn = sqlite3.connect('scores.db')


def create_scores_table():
    sql = """
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY,
            name TEXT,
            score INTEGER,
            accuracy REAL
        )
    """
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()


def add_score(name, score, accuracy):
    """Adds name, score, and player accuracy to the db"""
    sql = """
        INSERT INTO scores (name, score, accuracy)
        VALUES (?, ?, ?)
    """
    cursor = conn.cursor()
    cursor.execute(sql, [name, score, accuracy])
    conn.commit()




def run():
    """This function runs the main game menu, which includes instructions, play function, view leaderboard, and quit function"""

    create_scores_table()

    while True:
        prompt = """
        ~Around the Hello, World~
A python/basketball crossover (ha!) cli game!

Around the Hello, World is a game that tests your knowledge on python. 

How to play:

There are TEN spots, on the court Five TWO-POINT shots, and Five THREE-POINT shots.
You will start with the Five TWO-POINT shots first, and slowly work your way up to the three point line shots.

- Every time you get an easy question right on the first try, you get TWO points!
- Every time you get a hard question right on the first try, you get THREE points!

If you get the question wrong, you will stay in the same spot on the court, and will get a new question. If you get that right,
you will advance, but you will not get any points for the spot.

You can only progress towards the end of the game every time you get the questions right.

Have fun, try to cash in points, and be as accurate as possible from the field!

Select an option:
1. Play the game
2. Peep the leaderboard
3. Quit aka please no more puns
>> """
        option = input(prompt)
        if option == "1":
            play()
        elif option == "2":
            show_leaderboard()
        else: 
            print("This game broke my ankles")
            exit()

    

def play():
    """Runs when user selects Play Game from main game menu..."""
    def attempt_and_score():
    """Runs when a user attempts a question, function also keeps track of number of attempts and score if correct/incorrect"""
    score = 0
    attempt = 1
    correct_answer = "B" # or correct_answer = questions_answers[1].answer_key ??


    # Example code
    while True:
        print("What is the correct way to declare a function in Python? A: Function B: Def C: Func D: Declare")
        user_answer = input("Enter the correct answer: ").upper()
        
        if user_answer not in ["A", "B", "C", "D"]:
            print("")
            print("To answer this question, enter only using 'A', 'B', 'C', or 'D'")
            print("")
            continue
        
        if user_answer == correct_answer:
            score += 2
            print("")
            print(f"Correct! You've earned TWO points! Your current score is: {score}!!")
            print("")
            break
        else:
            score -= 1
            attempt += 1
            print("")
            print(f"Incorrect, please try again. Your current score is: {score}, and you are on attempt number {attempt}.")
            print("")


def show_leaderboard():
    """ Function successfully pulls scores/names/etc from leaderboard
    Runs when user selects Leaderboard from main game menu..."""
    pass

def post_points_to_scores_db():
    """Successfully posts points to scores database"""

def access_questions():
    """Function successfully pulls questions, options and answer keys from db"""
    pass

def post_points_to_questions_database():
    """Function successfully posts attempts and points for specific question to db to track if questions are actually easy / hard"""
    pass

def quit():
    """Runs when user selects quit from main game menu..."""
    pass


if __name__ == '__main__':
    run()