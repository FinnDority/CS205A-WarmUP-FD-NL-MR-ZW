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

        for i in user_input:

            if (i == 'rank'):
                key_words.append(i)
                print(user_input.index(i))
                value_words.append(i)
                print(value_words)

            elif (i == 'player_name'):
                key_words.append(i)
                print(user_input.index(i))
                value_words.append(i)
                print(value_words)

            elif (i == 'position'):
                key_words.append(i)
                print(user_input.index(i))
                value_words.append(i)
                print(value_words)

            elif (i == 'team'):
                key_words.append(i)
                print(user_input.index(i))
                value_words.append(i)
                print(value_words)

            elif (i == 'team_name'):
                key_words.append(i)
                print(user_input.index(i))
                value_words.append(i)
                print(value_words)

            elif (i == 'location'):
                key_words.append(i)
                print(user_input.index(i))
                value_words.append(i)
                print(value_words)

            elif (i == 'stadium'):
                key_words.append(i)
                print(user_input.index(i))
                value_words.append(i)
                print(value_words)

            elif (i == 'capacity'):
                key_words.append(i)
                print(user_input.index(i))
                value_words.append(i)
                print(value_words)

            elif (i == 'confrence'):
                key_words.append(i)
                print(user_input.index(i))
                value_words.append(i)
                print(value_words)

            elif (i == 'region'):
                key_words.append(i)
                print(user_input.index(i))
                value_words.append(i)
                print(value_words)

# Main function to run the user input function.
def main():

    user_input()


# start of the main function
main()
