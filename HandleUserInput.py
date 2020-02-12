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
def user_input():

        key_words = []
        value_words = []

        print('Welcome to the NFL teams database\n'
	        + 'You will be prompted below to enter information'
	        + ' about players and teams.')

        print('Please enter your query below.')

        user_input = input()
        user_input = user_input.split()

       """
       This loop will just go through the list and add the key with its values to new lists
       It's also easier to have the user input the players names without any spaces so then
       the two lists have the key words and values synced at the same indexes.
       """
        for i in user_input:

            if (i == 'rank'):
                key_words.append(i)
                value_words.append(user_input[user_input.index(i) + 1])

            elif (i == 'player_name'):
                key_words.append(i)
                value_words.append(user_input[user_input.index(i) + 1])

            elif (i == 'position'):
                key_words.append(i)
                value_words.append(user_input[user_input.index(i) + 1])

            elif (i == 'team'):
                key_words.append(i)
                value_words.append(user_input[user_input.index(i) + 1])

            elif (i == 'team_name'):
                key_words.append(i)
                value_words.append(user_input[user_input.index(i) + 1])

            elif (i == 'location'):
                key_words.append(i)
                value_words.append(user_input[user_input.index(i) + 1])

            elif (i == 'stadium'):
                key_words.append(i)
                value_words.append(user_input[user_input.index(i) + 1])

            elif (i == 'capacity'):
                key_words.append(i)
                value_words.append(user_input[user_input.index(i) + 1])

            elif (i == 'confrence'):
                key_words.append(i)
                value_words.append(user_input[user_input.index(i) + 1])

            elif (i == 'region'):
                key_words.append(i)
                value_words.append(user_input[user_input.index(i) + 1])

# Main function to run the user input function.
def main():

    user_input()


# start of the main function
main()
