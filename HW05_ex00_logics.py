#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    while True:
        userInput = raw_input("Please enter a number: ")

        try:
            userInputInt = int(userInput)
        except:
            print "It is not a Number!!"  
        else:
            break
    if(userInputInt % 2 == 0):
        print "The number is even."
    else:
        print "The number is odd."





def ten_by_ten():
    """ Prints integers 1 through 100 sequentially in a ten by ten grid."""
    n = 1
    while n<=100:
        if n%10 == 0:
            print n
        else:
            if n < 10:
                print str(n) + " ",
            else:
                print n,
        n = n+1


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    numberOfElements = 0
    sumOfElements = 0

    while True:
        userInput = raw_input("Please enter a number: ")

        if userInput == "done":
            break
        else:
            try:
                userInputInt = int(userInput)
            except:
                print "Please enter only numbers!!" 
            else:
                numberOfElements += 1
                sumOfElements += userInputInt
    if numberOfElements>0 and sumOfElements>0:
        averageOfNumbers = float(sumOfElements)/float(numberOfElements)
    else:
        averageOfNumbers = 0 

    print "The average of the numbers is: " + str(averageOfNumbers)



##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    even_odd()
    ten_by_ten()
    find_average()

if __name__ == '__main__':
    main()
