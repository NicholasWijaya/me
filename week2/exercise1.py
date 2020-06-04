lear"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# assign a list to some_words
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# print the some_words list one-by-one
for word in some_words:    # prints /n what /n does /n this/n line /n do /n ?
    print(word)

# same as the loop above, with 'x' as the counter instead of 'word'
for x in some_words:    # prints /n what /n does /n this/n line /n do /n ?
    print(x)

# print some_words as a list
print(some_words)     #  prints ['what', 'does', 'this', 'line', 'do', '?']

# if some_words list has more than 3 elements, print 'some_words contains more than 3 words'
if len(some_words) > 3:    # prints 'some_words contains more than 3 words'
    print('some_words contains more than 3 words')

# prints out info about machine running this function
def usefulFunction():   # prints 'uname_result(system='Windows', node='DESKTOP-2IDAAFA', release='10', version='10.0.18362', machine='AMD64', processor='Intel64 Family 6 Model 158 Stepping 9, GenuineIntel')'
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
