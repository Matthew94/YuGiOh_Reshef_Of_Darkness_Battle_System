from random import shuffle

def shuffle_decks(players):
    """Shuffles the deck and returns it."""
    shuffle(players[0].deck)
    shuffle(players[1].deck)
    return players

def print_and_get_player_move():
    """Prints all possibel moves and asks for the player's choice."""

    print("""
####################    ###################   #############################
##     Player     ##    ##      Hand     ##   ##         Field           ##
####################    ###################   #############################
-2: Surrender           1: View hand          5: View full field
-1: End Turn            2: See card details   6: View your own field
0:  Check life points   3: Discard Card       7: See card details
                        4: Play Card          8: Attack with card
                                              9: Sacrifice a card
                                              10: Set a card to defence mode
                                              11: Use effect of card
                                              12: Activate Magic Card
                                              13: Discard Card""")
    return input("Make a choice: ")

def print_hand(hand):
    """Prints the title and type of each card in the hand."""
    for index, card in enumerate(hand):
        print("{0}: {1} ({2})".format(index, card.title, card.type))

def print_hand_card_details(hand):
    """Asks player which card they want a detailed description of."""
    print_hand(hand)
    card = int(input("Which card do you want the details of?\nCard: "))
    print
    print_card_details(hand[card])

def place_card_on_board(player_board, card, normal_summoned):
    """Places a card on the first available slot on the board.
    
    Be sure to remove the card afterwards."""
    print("Playing: {0} ({1})".format(card.title, card.type))

    board_side = 0 if card.type == "Monster" else 1
    
    if normal_summoned == True and board_side == 0:
        print("You have already played a monster card.")
        return player_board, False

    for i in range(len(player_board[board_side])):
        if player_board[board_side][i] == None:
            player_board[board_side][i] = card
            break
        if player_board[board_side][4] != None:
            print("No spare slots for that card.")
            return player_board, False
    return player_board, True