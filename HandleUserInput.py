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
        SPECIAL_FUNCTIONS = ['help', 'load data', 'quit']
        key_words = []
        value_words = []



        user_in = input("Query: ")
        user_in = user_in.replace('%', '')
        while user_in != '' and not any(word in user_in for word in KEYS) and user_in not in SPECIAL_FUNCTIONS:
            user_in = input("Please enter a valid entry: ")


        if user_in.lower() == "help":
            help()
            return [],[]


        elif user_in.lower() == "load data":
            load()
            return [], []

        # call load data function
        elif user_in.lower() == "quit":
            exit(0)


        user_in = user_in.split("\"")

        for i in user_in:
                for j in KEYS:
                        if j in i:
                                if i not in key_words:
                                        key_words.append(i)
                                        try:
                                            value_words.append(user_in[user_in.index(i) + 1])
                                        except:
                                            print("Invalid query. Expected specific value after " + i)

        for i in range(len(key_words)):
                test = key_words[i].split()
                for j in test:
                        if j not in KEYS:
                                print("Your entered a keyword that was not valid.")
                                return [], []
        if len(key_words[0].split() + key_words[1:]) <= 1:
            print("Invalid query. Please enter both display column(s) and search criteria.")
            return [], []

        for i in key_words[0].split():
                if i == "team_name":
                        i = "t.team_name"
                        print(i)

        return key_words[0].split() + key_words[1:],  value_words

# Main function to run the user input function.

def parse_user_input(key_words, value_words):
    if key_words == [] or value_words == []:
        return
    
    db_file = "football.db"
    conn = sqlite3.connect(db_file)
    if (len(key_words) > 1):
        command = "SELECT "
        command += key_words[0]
        command += " FROM teams t, players p"
        command += " WHERE t.team_name = p.team_name"
        for i in range(1, len(key_words)):
            command += " AND " + key_words[i]
            command += "=\""
            if (i > len(value_words)):
                print("ERROR, VALUES NOT PROVIDED")
                command += "*"
            else:
                command += (value_words[i-1].lower())
            command += "\""
        print(command)
        # cursor = conn.execute(command)
        c = conn.cursor()
        for row in c.execute(command):
            print(row)

    conn.close()


def main():
    print   ('Welcome to the NFL teams database\n'
	        + 'You will be prompted below to enter information'
        + ' about players and teams.'
        + '\nIf you need help please type: help'
        + '\nPlease enter your query below.\n')


    while True:
        keys, values = user_input()
        parse_user_input(keys, values)


# start of the main function
main()
