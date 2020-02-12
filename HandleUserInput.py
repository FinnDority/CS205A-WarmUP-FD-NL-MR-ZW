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
import FrontEnd

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
            exit(0)
        # call load data function
        if user_in.lower() == "quit":
            exit(0)


        user_in = user_in.split()

        """
        This loop will just go through the list and add the key with its values to new lists
        It's also easier to have the user input the players names without any spaces so then
        the two lists have the key words and values synced at the same indexes.
        """
        for i in user_in:
            for j in range(0, len(KEYS)):
                if (i == KEYS[j]):
                    key_words.append(i)
                    value_words.append(user_in[user_in.index(i)])

        print(key_words)
        print(value_words)

# Main function to run the user input function.
def main():

    user_input()


# start of the main function
main()
