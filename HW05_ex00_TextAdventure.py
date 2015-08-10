#!/usr/bin/env python
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit
import sys

# Body


def infinite_stairway_room(userName, count=0):
    print "{0} walks through the door to see a dimly lit hallway.".format(userName)
    print "At the end of the hallway is a", count * 'long ', 'staircase going towards some light'
    print "There is a door to the left with screams coming from within."
    print "What does {0} do?".format(userName)
    next = raw_input("> ")
    
    # infinite stairs option
    if "take" in next or "stairs" in next:
        print '{0} takes the stairs'.format(userName)
        if (count > 0):
            print "but {0} is not happy about it".format(userName)
        infinite_stairway_room(userName, count + 1)
    if "open" in next or "door" in next or "left" in next:
        gold_room(userName)
    elif "turn" in next or "back" in next:
        bear_room(userName)
    else:
        print "Think up of something fast."


def gold_room(userName):
    print "This room is full of gold.  How much does {0} take?".format(userName)

    next = raw_input("> ")
    try:
       how_much = int(next)
    except:
       dead("Man, learn to type a number.")
    
    if how_much < 50:
        print "Nice, {0} is not greedy, {0} wins!".format(userName)
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room(userName):
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How is {0} going to move the bear?".format(userName)
    bear_moved = False

    while True:
        next = raw_input("> ")

        if "take" in next or "honey" in next:
            dead("The bear looks at {0} then slaps {0}'s face off.".format(userName))
        elif "taunt" in next and not bear_moved:
            print "The bear has moved from the door. {0} can go through it now.".format(userName)
            bear_moved = True
        elif "taunt" in next and bear_moved:
            dead("The bear gets pissed off and chews {0}'s leg off.".format(userName))
        elif ("open" in next or "door" in next) and bear_moved:
            infinite_stairway_room(userName, 0)
        else:
            print "I got no idea what that means."


def cthulhu_room(userName):
    print "Here {0} sees the great evil Cthulhu.".format(userName)
    print "He, it, whatever stares at {0} and {0} goes insane.".format(userName)
    print "Does {0} flee for your life or eat {0}'s head?".format(userName)

    next = raw_input("> ")

    if "flee" in next:
        start(userName)
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room(userName)


def dead(why):
    print why, "Good job!"
    exit(0)

def start(userName):
    print "{0} is in a dark room.".format(userName)
    print "There is a door to {0}'s right and left.".format(userName)
    print "Which one does {0} take?".format(userName)

    next = raw_input("> ")

    if next == "left":
        bear_room(userName)
    elif next == "right":
        cthulhu_room(userName)
    elif next == "back":
        back_room(userName)
    else:
        dead("{0} stumbles around the room until {0} starves.".format(userName))

def back_room(userName):
    print "{0} has entered a room full of awkward programmers.".format(userName)
    print "{0} states his name but nobody listens.".format(userName)
    print "{0} starts programming python and never leaves.".format(userName)
    exit(0)


##############################################################################
def main():
    # START the TextAdventure game

    userName = sys.argv[1]
    start(userName)


if __name__ == '__main__':
    main()
