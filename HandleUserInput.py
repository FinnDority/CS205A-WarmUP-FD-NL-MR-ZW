def user_input():

        print('Welcome to the NFL teams database\n'
	        + 'You will be prompted below to enter information'
	       + ' about players and teams.')
        print('**********************************************')

        print('Please enter your query below.')

        user_input = input()
        user_input = user_input.split()
        print(user_input)

# Main function to run the user input function.
def main():

    user_input()

main()




















def split_input(user_input):
    input_list = user_input.split()
    for word in input_list:










