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

def user_input():
        KEYS = ["rank", "player_name", "position", "team_name", "location", "stadium", "capacity", "conference", "region"]
        SPECIAL_FUNCTIONS = ['help', 'load data', 'quit']
        key_words = []
        value_words = []

        user_in = input("Query:")
        user_in = user_in.replace('%', '')
        user_in = user_in.lower()
        while user_in != '' and not any(word in user_in for word in KEYS) and user_in not in SPECIAL_FUNCTIONS:
            user_in = input("Please enter a quiery wi")
            user_in = user_in.lower()

        if user_in.lower() == "help":
            help()
            user_input()

        elif user_in.lower() == "load data":
            load()
            return

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
                        elif j not in i:
                                print("That is not a valid keyword please enter a valid query.")
                                return

        print(key_words[0].split() + key_words[1:],  value_words)
        return key_words[0].split() + key_words[1:],  value_words

# Main function to run the user input function.
def main():
    print   ('Welcome to the NFL teams database\n'
	        + 'You will be prompted below to enter information'
        + ' about players and teams.'
        + '\nIf you need help please type: help'
        + '\nPlease enter your query below.\n')

    while True:
        user_input()


# start of the main function
main()
