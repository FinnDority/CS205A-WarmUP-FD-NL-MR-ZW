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

        print('Welcome to the NFL teams database\n'
	        + 'You will be prompted below to enter information'
            + ' about players and teams.')

        print('Please enter your query below.')

        user_in = input()

        user_in = user_in.replace('%', '')

        if user_in.lower() == "help":
            help()
        if user_in.lower() == "load data":
            load()
        if user_in.lower() == "quit":
            exit(0)


        user_in = user_in.split()

        """
        This loop will just go through the list and add the key with its values to new lists
        It's also easier to have the user input the players names without any spaces so then
        the two lists have the key words and values synced at the same indexes.
        """


# Main function to run the user input function.
def main():

    user_input()


# start of the main function
main()
