"""
KeyWords
rank
player_name
position
team_name
location
stadium
capacity
confrence
region
"""
from FrontEnd import load, help
import sqlite3

def user_input():
        KEYS = ["rank", "player_name", "position", "team_name", "location", "stadium", "capacity", "conference", "region"]
        key_words = []
        value_words = []



        user_in = input()

        user_in = user_in.replace('%', '')

        if user_in.lower() == "help":
            help()
            user_input()
        elif user_in.lower() == "load data":
            load()
        # call load data function
        elif user_in.lower() == "quit":
            exit(0)


        user_in = user_in.split("\"")

        for i in user_in:
                for j in KEYS:
                        if j in i:
                                if i not in key_words:
                                        key_words.append(i)
                                        value_words.append(user_in[user_in.index(i) + 1])

        return key_words[0].split() + key_words[1:],  value_words

# Main function to run the user input function.

def parse_user_input(key_words, value_words):
    db_file = "football.db"
    conn = sqlite3.connect(db_file)
    command = "SELECT "
    command += key_words[0]
    command += " FROM teams t, players p"
    if (len(key_words) > 1):
        for i in range(1, len(key_words)):
            command += " WHERE "
            command += 


    # cursor = conn.execute()
    conn.close()


def main():
    print   ('Welcome to the NFL teams database\n'
	        + 'You will be prompted below to enter information'
        + ' about players and teams.'
        + '\nIf you need help please type: help'
        + '\nPlease enter your query below.\n')

    parse_user_input(user_input())


# start of the main function
main()
