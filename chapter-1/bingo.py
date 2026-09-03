#imports and global variables
import random

MAX_NUM = 10
MIN_NUM = 1
max_guess_counts = 3
#generate a random number 
def generate_random_num():
    return random.randint(MIN_NUM,MAX_NUM)

#get user input as guess
def get_user_input():
    print(f"your number should be between {MIN_NUM}-{MAX_NUM}")
    while True:
        try:
            user_input =int(input("enter your guess: "))
        except ValueError:
            print("Error: Enter a valid number.")
        else:
            return user_input
        
#ckeck guessed number
def ckeck_guessed_number(user_input, random_num):
    return user_input == random_num

#main function for running application
def main():
    global max_guess_counts
    random_num = generate_random_num()
    # print(f"random number is: {random_num}")
    while max_guess_counts > 0:
        user_input =get_user_input()
        if ckeck_guessed_number(user_input, random_num):
            print("You have guess right.")
            break
        max_guess_counts-=1
        print(f"guesses left: {max_guess_counts}")
    else:
        print("you could not guess the number, and ran out of guesses.")

if __name__ == "__main__":
    main()
