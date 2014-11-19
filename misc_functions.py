from __future__ import print_function
from random import randint

from player_functions import print_hand

def print_intro_text():
    print("It's time to Duh-Duh-Duh-Duh-D-D-D-D-D-D-D-D-Duelllllll!!!!!!")

def coin_toss():
    """Randomly returns a 0 or 1"""
    toss = randint(0,1)
    print("Player {0} is first.\n".format(toss + 1))

    return toss

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

def declare_winner(players):
    """Checks life points of each player and prints the winner.
    
    Checks for a draw first then decides the winner.
    """

    if players[0].life_points == players[1].life_points == 0:
        print("It's a draw!")
    else:
        winner = 2
        if players[0].life_points:  # Check > 0 
            winner = 1
        print("\nPlayer {0} has won!".format(winner))

def discard_excess_from_hand(hand):
    if len(hand) > 5:
        print_hand(hand)
        discard = int(input("You have too many cards.\nChoose one to discard: "))
        print("Discarding {0}...".format(hand[discard].title))
        del hand[discard]
    return hand

def starting_draw(players):
    """Makes both players draw 5 cards."""

    print("\nPlayer 1 starting draw.")
    for i in range(5):
        draw_card(players[0])
    print("\nPlayer 2 starting draw.")
    for i in range(5):
        draw_card(players[1])
    print()

def draw_card(player):
    """Adds the top card from the deck to the hand."""

    player.hand.append(player.deck[0])
    print("Player {0} drew a [{1}].".format(player.number + 1,
                                          player.deck[0].title))
    del player.deck[0]