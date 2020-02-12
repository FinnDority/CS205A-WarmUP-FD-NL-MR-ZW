"""
KeyWords
rank
plyer_name
position
team
team_name
location
stadium
capacity
confrence
region
"""
from FrontEnd import load, help

def user_input():
        KEYS = ["rank", "player_name", "position", "team", "team_name", "location", "stadium", "capacity", "conference", "region"]
        key_words = []
        value_words = []

        print   ('Welcome to the NFL teams database\n'
	        + 'You will be prompted below to enter information'
                + ' about players and teams.'
                + '\nIf you need help please type: help.'
                + '\nPlease enter your query below.\n')

        user_in = input()

        user_in = user_in.replace('%', '')

        if user_in.lower() == "help":
            help()
            user_input()
        if user_in.lower() == "load data":
            load()
            exit(0)
        # call load data function
        if user_in.lower() == "quit":
            exit(0)


        user_in = user_in.split("\"")

        for i in user_in:
                for j in KEYS:
                        if j in i:
                                if i not in key_words:
                                        key_words.append(i)
                                        value_words.append(user_in[user_in.index(i) + 1])

        print(value_words)
        print(key_words)


# Main function to run the user input function.
def main():

    user_input()


# start of the main function
main()
