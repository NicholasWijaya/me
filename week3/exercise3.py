"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random
import sys

def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    counter = 0
    while counter < 1:
        input_to_check = input(message)
        
        if input_to_check == 'end':   #'end' is keyword to end the running program
            sys.exit('******************program ended******************')
        
        abs_input = input_to_check.lstrip('-')    #remove '-' when testing negative numbers
        if abs_input.isdigit() == False:    #test if input is integer type
            print('! Only integers allowed !')
            continue
        else:
            break
                
    return int(input_to_check)

def boundary_validator():
    counter = 0
    while counter < 1:
        lower_bound = not_number_rejector('Please enter a lower bound: ')
        upper_bound = not_number_rejector('Please enter an upper bound: ')

        if lower_bound >= upper_bound:   #check that lower bound is less than upper bound
            print('! Upper bound must be greater than lower bound !')
            continue  
        else:
            break 

    return lower_bound, upper_bound

def guess_checker(guess_this_number,lower_bound,upper_bound):
    guessed = False

    while not guessed:
        user_guess = not_number_rejector('Please enter a guess: ')
        if lower_bound <= user_guess <= upper_bound:
            if user_guess < guess_this_number:
                print('! Your guess is too low !')
            elif user_guess > guess_this_number:
                print('! Your guess is too high !')
            else:
                guessed = True
        else:
            print('! Your guess is out of bounds !')
            continue
    
    return guessed

def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 2, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("*** Welcome to The Guessing Game ***\nGuess a random number within the boundaries you input")
    
    bounds = boundary_validator()   #asks for valid lower/upper bounds 
    lower_bound = bounds[0]
    upper_bound = bounds[1]       
    print('The number rolled is between {} and {}'.format(lower_bound,upper_bound))

    guess_this_number = random.randint(lower_bound,upper_bound)     #roll a random integer within the bounds given
    
    guess_checker(guess_this_number,lower_bound,upper_bound)       #asks for a guess, keeps asking until correct.
    
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
