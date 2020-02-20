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

# the ultimate sin: a global variable oh god
conn = 0  # 0 acts as a sentinel value
loaded = 0

def user_input():
        global conn
        global loaded
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
            loaded = 1
            load()
            return [], []

        # call load data function
        elif user_in.lower() == "quit":
            if conn != 0:
                conn.close()
            exit(0)
        
        if loaded == 0:
            print("User must load the database before asking a query.")
            return [], []

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

        new_keys = key_words[0].split()
        if "team_name" in new_keys:
            index = new_keys.index("team_name")
            new_keys[index] = "t.team_name"
            key_words[0] = ""
            for i in range(len(new_keys)):
                key_words[0] += " " + new_keys[i]

        return key_words[0].split() + key_words[1:],  value_words

# Main function to run the user input function.

def parse_user_input(key_words, value_words):
    global conn
    if key_words == [] or value_words == []:
        return

    if (conn == 0):
        db_file = "football.db"
        conn = sqlite3.connect(db_file)

    if (len(key_words) > 1):
        command = "SELECT "
        command += key_words[0]
        if len(key_words) > (len(value_words)+1):
            for i in range(1, len(key_words)-len(value_words)):
                command += ", "
                command += key_words[i]

        command += " FROM teams t, players p"
        command += " WHERE t.team_name = p.team_name"
        j = 0
        for i in range(len(key_words)-len(value_words), len(key_words)):
            command += " AND " + key_words[i]
            if (j > len(value_words)):
                print("ERROR, VALUES NOT PROVIDED")
                command += "*"
            else:
                if (value_words[j][0] != "<" and value_words[j][0] != ">"):
                    command += "=\""
                    command += (value_words[j].lower())
                    command += "\""
                else:
                    command += (value_words[j].lower())
            j += 1

        print(command)
        # cursor = conn.execute(command)
        c = conn.cursor()
        for row in c.execute(command):
            print(row)


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
