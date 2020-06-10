# -*- coding: UTF-8 -*-
"""Week 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=1):
    """Return a list of numbers between start and stop in steps of step.

    Do this using any method apart from JUST using range()
    The look up the docs for range(), you can answer this with just the range 
    function, but we'd like you to do it the long way, probably using a loop.
    """
    numlist0 = []
    loop = 0
    while loop <= int((stop-start-1)/step):     #-1 because excluding stop number, just like in range()
        numlist0.append(start+step*loop)
        loop += 1
    return numlist0


def lone_ranger(start, stop, step):
    """Duplicate the functionality of range.

    Look up the docs for range() and wrap it in a 1:1 way
    """

    return list(range(start,stop,step))


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2
    """
    step = 2
    loop = 0
    numlist2 = []
    while loop <= int((stop-start-1)/step):        #-1 because excluding stop number, just like in range()
        numlist2.append(start+step*loop)
        loop += 1
    return numlist2


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for input
    """
    counter = 0
    while counter < 1:
        numinput0 = float(input('Please enter a number:'))

        if numinput0 < low or numinput0 > high:
            print('Number out of bounds!')
        else:
            break
                    
    return numinput0


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    counter = 0
    while counter < 1:
        numinput1 = input(message)

        try:
          float(numinput1)
        except:
          print('! Only numbers are accepted !')
          continue

        break
    return numinput1


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    counter = 0
    while counter < 1:
        numinput2 = float(not_number_rejector('Please enter a number: '))
        
        if numinput2 < low or numinput2 > high:
            print('Number out of bounds!')
        else:
            break
    
    
    return numinput2


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\nlone_ranger", lone_ranger(1, 10, 3))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
