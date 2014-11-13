from random import randint, shuffle

try:
    input = raw_input
except:
    pass

class Card(object):
    def __init__(self, title = "Dark Magician", type = "Monster"):
        self.title = title
        self.short_title = self.create_short_title(title)
        self.attack = 2500
        self.defence = 2100
        self.type = type
        self.description = "I am a card."
        
    def create_short_title(self, title):
        length = len(title)
        # If it's a long title, shorten it
        if length >= 10:
            return "[{0}]".format(title[0:10])
        # If it's short, add whitespace
        else:
            start = "["
            end = ""
            # Work out how much whitespace is needed
            white_space = 10 - length
            white_iter = int(white_space / 2)
            # If it's an even amount, add the same to each side
            if white_space % 2 == 0:
                for i in range(white_iter):
                    start += " "
                    end += " "
                end += "]"
                return start + title + end
            # Else have one more blank char to the left
            else:
                for i in range(white_iter):
                    start += " "
                    end += " "
                end += " ]"
                return start + title + end

class Player(object):
    def __init__(self, number = "0"):
        self.number = number
        self.life_points = 8000
        self.hand = []
        self.deck = [Card("Jim","Magic"), Card("Tom","Trap"), Card("Harry"),
                     Card("Bob","Trap"), Card("Ollie","Magic"), Card("Jimmy"),
                     Card("Sam"), Card("pop","Magic"), Card("Matthew","Trap"),
                     Card("Corner"), Card("Ross"), Card("Datasheet"),
                     Card("Cor-ner"), Card("Oven","Magic"), Card("Microwave"),
                     Card("Earl","Trap"), Card("lel"), Card("Kek","Magic")]

def begin_battle():
    """Program to simulate a battle from Yu-Gi-Oh: Reshef of Destruction.

    players: list of two player objects
    board: list with two lists that each have two lists of 5 slots
    """
    print("It's time to Duh-Duh-Duh-Duh-D-D-D-D-D-D-D-D-Duelllllll!!!!!!")

    # Setting up players
    players = [Player(0),Player(1)]
    players = shuffle_decks(players)

    # Setting up board
    board = [[[None] * 5, [None] * 5], [[None] * 5, [None] * 5]]

    starting_draw(players)

    print("\nBattle starting.")
    battle_loop(players, board)

    declare_winner(players)

def declare_winner(players):
    winner = 2
    if(players[0].life_points > 0):
        winner = 1
    print("\nPlayer {0} has won!".format(winner))

def battle_loop(players, board):
    i = coin_toss()
    print("Player {0} is first.\n".format(i + 1))

    while(players[0].life_points > 0 and players[1].life_points > 0):
        j = i % 2

        print("##Player {0}'s turn.##".format(players[j].number + 1))
        draw_card(players[j])

        players[j], board = player_move(players[j], board)

        players[j].life_points = 0

def draw_card(player):
    """Adds the top card from the deck to the hand."""
    player.hand.append(player.deck[0])
    print("Player {0} drew a [{1}].".format(player.number + 1,
                                          player.deck[0].title))
    del player.deck[0]

def starting_draw(players):
    """Makes both players draw 5 cards."""
    print("\nPlayer 1 starting draw.")
    for i in range(5):
        draw_card(players[0])
    print("\nPlayer 2 starting draw.")
    for i in range(5):
        draw_card(players[1])
    print

def shuffle_decks(players):
    """Shuffles the deck and returns it."""
    shuffle(players[0].deck)
    shuffle(players[1].deck)
    return players

def coin_toss():
    """Randomly returns a 0 or 1"""
    return randint(0,1)

def player_move(player, board):
    normal_summoned = False

    while(1):
        move  = get_player_move()

        # Player moves
        # End turn
        if move == '-1':
            break
        # Print lift points
        elif move == '0':
            print("\nYou have {0} "
                  "life points.".format(player.life_points))
        
        # Hand moves
        # Print hand
        elif move == '1':
            print_hand(player.hand)
        # See card details
        elif move == '2':
            print_hand_card_details(player.hand)
        # Discard card from hand
        elif move == '3':
            print_hand(player.hand)
            choice = int(input("Delete card: "))
            if choice == -1:
                continue
            del player.hand[choice]
        # Play card to field
        elif move == '4':
            print_hand(player.hand)
            choice = int(input("Play card: "))

            board[player.number], was_played = place_card_on_board(
                board[player.number], player.hand[choice])

            if was_played == True:
                del player.hand[choice]
        
        # Field Moves
        # View the field
        elif move == '5':
            print_board(board)
        # See card details
        elif move == '6':
            pass
        # Attack with a card
        elif move == '7':
            pass
        # Sacrafice a card
        elif move == '8':
            pass
        # Set card to defence mode
        elif move == '9':
            pass
        # Use card effect
        elif move == '10':
            pass
        # Activate a magic card
        elif move == '11':
            pass
        # Discard a card
        elif move == '12':
            pass
    return player, board

def get_player_move():
    print("""
####################    ###################   #############################
##     Player     ##    ##      Hand     ##   ##         Field           ##
####################    ###################   #############################
-1: End Turn            1: View hand          5: View field
0: Check life points    2: See card details   6: See card details
                        3: Discard Card       7: Attack with card
                        4: Play Card          8: Sacrafice a card
                                              9: Set a card to defence mode
                                              10: Use effect of card
                                              11: Activate Magic Card
                                              12: Discard Card""")
    return input("Make a choice: ")

def print_hand(hand):
    """Prints the title and type of each card in the hand."""
    for index, card in enumerate(hand):
        print("{0}: {1} ({2})".format(index, card.title, card.type))

def print_hand_card_details(hand):
    print_hand(hand)
    card = int(input("Which card do you want the details of?\nCard: "))
    print
    print_card_details(hand[card])

def print_card_details(card):
    print("Title: [{0}]".format(card.title))
    print("Type: [{0}]".format(card.type))
    print("Description: {0}".format(card.description))
    if card.type == "Monster":
        print("Attack: [{0}]".format(card.attack))
        print("Defence: [{0}]".format(card.defence))
    else:
        pass

def print_board(board):
    """Works"""
    board_txt = ["","","",""]

    for i, side in enumerate(board):
        for j, type in enumerate(side):
            for card in type:
                if card == None:
                    board_txt[(i * 2) + j] += "[ Nil card ] "
                else:
                    board_txt[(i * 2) + j] += "{0} ".format(card.short_title)

    print("""
Player One:
Spell: {0}
Monst: {1}

Monst: {2}
Spell: {3}
Player 2:
""".format(board_txt[1], board_txt[0], board_txt[2],
                    board_txt[3]))

def place_card_on_board(player_board, card):
    """Places a card on the first available slot on the board.
    
    Be sure to remove the card afterwards."""
    print("Playing: {0} ({1})".format(card.title, card.type))

    board_side = 0 if card.type == "Monster" else 1
        
    for i in range(len(player_board[board_side])):
        if player_board[board_side][i] == None:
            player_board[board_side][i] = card
            break
        if player_board[board_side][4] != None:
            print("\nNo spare slots\n")
            return player_board, False
    return player_board, True

if __name__ == '__main__':
    begin_battle()