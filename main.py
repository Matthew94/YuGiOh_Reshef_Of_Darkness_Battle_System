from random import randint, shuffle

try:
    input = raw_input
except:
    pass

class Card(object):
    def __init__(self, title = "Dark Magician", type = "Monster"):
        self.title = title
        self.attack = 2500
        self.type = type

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
    players = [Player("1"),Player("2")]
    players = shuffle_decks(players)

    # Setting up board
    board = [[[None] * 5, [None] * 5], [[None] * 5, [None] * 5]]

    starting_draw(players)

    print("\nBattle starting.")
    battle_loop(players, board)

    declare_winner(players)

def battle_loop(players, board):
    i = coin_toss()
    print("Player {0} is first.\n".format(i + 1))

    while(players[0].life_points > 0 and players[1].life_points > 0):
        j = i % 2

        print("##Player {0}'s turn.##".format(players[j].number))
        draw_card(players[j])

        choose_move(players, j, board)

        players[j].life_points = 0

def choose_move(players, j, board):
    while(1):
        move  = get_move(players[j])

        # Player moves
        if move == '-1':
            break
        elif move == '0':
            print("\nYou have {0} "
                  "life points.".format(players[j].life_points))
        elif move == '1':
            print_hand(players[j])
        # Hand moves
        elif move == '2':
            print_hand_card_details(players[j])
        # Field Moves

def get_move(player):
    print("""
####################    ###################   #############################
##     Player     ##    ##      Hand     ##   ##         Field           ##
####################    ###################   #############################
-1: End Turn            1: View hand          5: View field
0: Check life points    2: See card details   6: See card details
                        3: Dicard Card        7: Attack with card
                        4: Play Card          8: Sacrafice a card
                                              9: Set a card to defence mode
                                              10: Use effect of card
                                              11: Activate Magic Card
                                              12: Discard Card""")
    return input("Make a choice: ")

def declare_winner(players):
    winner = 2
    if(players[0].life_points > 0):
        winner = 1
    print("\nPlayer {0} has won!".format(winner))


def place_card_on_board(board_side, hand, hand_pos, position):
    print("Playing: {0} ({1})".format(hand[hand_pos].title,
                                     hand[hand_pos].type))

    if hand[hand_pos].type == "Monster":
        board_side[0][position] = hand[hand_pos]
        del hand[hand_pos]
    elif hand[hand_pos].type == "Magic" or "Trap":
        board_side[1][position] = hand[hand_pos]
        del hand[hand_pos]

def print_board(board):
    """Works"""
    board_txt = ["","","",""]

    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(len(board[i][j])):
                if board[i][j][k] == None:
                    board_txt[(i * 2) + j] += "0\t"
                else:
                    board_txt[(i * 2) + j] += "1\t"

    print("""
Player One:
Spell: {0}
Monst: {1}

Monst: {2}
Spell: {3}
Player 2:
""".format(board_txt[1], board_txt[0], board_txt[2],
                    board_txt[3]))

def print_hand(player):
    """Prints the title and type of each card in the hand."""
    print("\nPlayer {0}'s hand:".format(player.number))
    for card in player.hand:
        print("{0} ({1})".format(card.title, card.type))

def print_hand_card_details(player):
    print_hand(player)

def draw_card(player):
    """Adds the top card from the deck to the hand."""
    player.hand.append(player.deck[0])
    print("Player {0} drew a [{1}].".format(player.number,
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

def old_coin_toss():
    """Asks player one to choose a coin.
    Returns 1 if player one is first.

    Returns 2 if neither is chosen.
    """
    roll = randint(0,1)

    choice = ""

    while choice != "heads" and "tails":
        choice = input("Player one: Heads or tails?\nChoice: ").lower()

    if choice == 'heads':
        choice = 1
    elif choice == 'tails':
        choice = 0

    if choice == roll:
        return 0
    else:
        return 1

if __name__ == '__main__':
    begin_battle()