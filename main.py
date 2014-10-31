from random import randint, shuffle

class Card(object):
    def __init__(self, title = "Dark Magician"):
        self.title = title
        self.attack = 2500

class Player(object):
    def __init__(self):
        self.life_points = 8000
        self.hand = []
        self.deck = [Card("Jim"), Card("Tom"), Card("Harry")]

def begin_battle():
    """Program to simulate a battle from Yu-Gi-Oh: Reshef of Destruction.

    players: list of two player objects
    board: list with two lists that each have two lists of 5 slots

    """
    # Setting up players
    players = [Player(),Player()]
    players = shuffle_decks(players)
    
    # Setting up board
    board = [[[None] * 5, [None] * 5], [[None] * 5, [None] * 5]]




def print_board(board):
    """Works"""
    board_txt = ["","","",""]

    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(len(board[i][j])):
                if board[i][j][k] == None:
                    board_txt[(i * 2) + j] += "0 "
                else:
                    board_txt[(i * 2) + j] += "1 "

    print("Player One:\n{0}\n{1}\n\n{2}\n{3}\n".format(
        board_txt[1], board_txt[0], board_txt[2], board_txt[3]))

def draw_card(player):
    pass
    
def shuffle_decks(players):
    """Works"""
    shuffle(players[0].deck)
    shuffle(players[1].deck)
    return players

def coin_toss():
    """Asks player one to choose a coin.
    Returns 1 if player one is first.

    Returns 2 if neither is chosen.
    """
    choice = input("Player one: Heads or tails?\nChoice: ").lower()
    print(choice)
    roll = randint(0,1)

    if choice == 'heads':
        choice = 1
    elif choice == 'tails':
        choice = 0
    else:
        return 2

    if choice == roll:
        return 1
    else:
        return 0

if __name__ == '__main__':
    begin_battle()