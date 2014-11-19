from __future__ import print_function

def print_intro_text():
    print("It's time to Duh-Duh-Duh-Duh-D-D-D-D-D-D-D-D-Duelllllll!!!!!!")

def coin_toss():
    """Randomly returns a 0 or 1"""
    return randint(0,1)

def print_card_details(card):
    """Prints all attributes of a card."""

    print("Title: [{0}]".format(card.title))
    print("Type: [{0}]".format(card.type))
    print("Description: {0}".format(card.description))
    if card.type == "Monster":
        print("Attack: [{0}]".format(card.attack))
        print("Defence: [{0}]".format(card.defence))
        
        mode = "Attack Mode"
        if card.defence_mode:
            mode = "Defence Mode"
        print("Mode: {0}".format(mode))