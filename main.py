from random import randint, shuffle

try:
    input = raw_input
except:
    pass

class Card(object):
    def __init__(self, title = "Dark Magician", type = "Monster"):
        """Contains the attributes of the card."""
        self.title = title
        self.short_title = self.create_short_title(title)
        self.attack = 2500
        self.defence = 2100
        self.type = type
        self.description = "I am a card."
        self.defence_mode = False
        self.face_down = True

    def create_short_title(self, title):
        """Creates a shortened title for displaying on the board."""
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
        """Object representing a player.

        Has life points, a deck and a hand.

        self.number is to make it easy to access it from a list.
        It would typically be 0 or 1.
        """

        self.number = number
        self.life_points = 8000
        self.hand = []
        self.deck = [Card("Jim","Magic"), Card("Tom","Trap"), Card("Harry"),
                     Card("Bob","Trap"), Card("Ollie","Magic"), Card("Jimmy"),
                     Card("Sam"), Card("pop","Magic"), Card("Matthew","Trap"),
                     Card("Corner"), Card("Ross"), Card("Datasheet"),
                     Card("Cor-ner"), Card("Oven","Magic"), Card("Microwave"),
                     Card("Earl","Trap"), Card("lel"), Card("Kek","Magic")]

def main():
    """Program to simulate a battle from Yu-Gi-Oh: Reshef of Destruction.

    players: list of two player objects
    board: list with two lists that each have two lists of 5 slots
    """
    print("It's time to Duh-Duh-Duh-Duh-D-D-D-D-D-D-D-D-Duelllllll!!!!!!")

    # Setting up players
    players = [Player(0),Player(1)]
    players = shuffle_decks(players)

    # Setting up board: Player 0 Monsters/Magic - Player 1 Monsters/Spells
    board = [[[None] * 5, [None] * 5], [[None] * 5, [None] * 5]]

    starting_draw(players)

    print("\nBattle starting.")
    battle_loop(players, board)

    declare_winner(players)

def declare_winner(players):
    """Checks life points of each player and prints the winner.
    
    Checks for a draw first then decides the winner.
    """

    if players[0].life_points == players[1].life_points == 0:
        print("It's a draw!")
    else:
        winner = 2
        if(players[0].life_points > 0):
            winner = 1
        print("\nPlayer {0} has won!".format(winner))

def battle_loop(players, board):
    """Main loop of battle.

    i is an int that can start at 0 or 1 and decides who goes first.
    It's incremented each turn.

    j is i % 2 so it ensures that you can still access the players
    from the lists even after i becomes greater than 1.

    The players draw a card and take their turns until one of them
    hits 0 life points.
    """

    i = coin_toss()
    print("Player {0} is first.\n".format(i + 1))

    while(players[0].life_points > 0 and players[1].life_points > 0):
        j = i % 2

        print("\n##Player {0}'s turn.##".format(players[j].number + 1))
        draw_card(players[j])

        players[j], board = do_player_move(players[j], board)

        # Check if the player has too many cards, discard one if over 5
        if len(players[j].hand) > 5:
            print_hand(players[j].hand)
            discard = int(input("You have too many cards.\nChoose one to discard: "))
            print("Discarding {0}...".format(players[j].hand[discard].title))
            del players[j].hand[discard]

        # TODO: Set all attack mode cards to face up
        

        # Move counter to next turn
        i += 1

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

def do_player_move(player, board):
    """Displays all possible moves then gets the players input.

    Calls the relevant function depending on the choice.

    Function ends when the player ends their turn.
    """
    normal_summoned = False
    sacrifices = 0

    while(1):
        move  = print_and_get_player_move()

        # Player moves
        # Surrender
        if move == "-2":
            player.life_points = 0
            break
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
            choice = int(input("(-1 to cancel) Delete card: "))
            if choice == -1:
                continue
            del player.hand[choice]
        # Play card to field
        elif move == '4':
            print_hand(player.hand)
            choice = int(input("Play card: "))

            board[player.number], was_played = place_card_on_board(
                board[player.number], player.hand[choice],
                normal_summoned)

            if was_played == True:
                if player.hand[choice].type == "Monster":
                    normal_summoned = True
                del player.hand[choice]
        
        # Field Moves
        # View the field
        elif move == '5':
            print_board(board)
        # See card details
        elif move == '6':
            print_player_board(board[player.number])
            choice = int(input("Choose a card: "))

            # If it's a magic/trap card set list index to 1
            if choice > 4:
                choice -= 5
                side = 1
            else:
                side = 0

            if board[player.number][side][choice] != None:
                print_card_details(board[player.number][side][choice])
            else:
                print("There is no card in that slot.")
        # Attack with a card
        elif move == '7':
            pass
        # sacrifice a card
        elif move == '8':
            print_player_monsters(board[player.number][0])
            choice = int(input("(-1 to quit)\nChoose a card to sacrifice: "))

            if choice == -1:
                continue

            if board[player.number][0][choice] is not None:
                print("Sacrificing {0}...".format(board[player.number][0][choice].title))
                board[player.number][0][choice] = None
                sacrifices += 1
            else:
                print("There is no card there...")

        # Set card to defence mode
        elif move == '9':
            print_player_monsters(board[player.number][0])
            choice = int(input("(-1 to quit)\nChoose a card to put into defence mode: "))

            if choice == -1:
                continue

            if board[player.number][0][choice] is not None:
                board[player.number][0][choice].defence_mode = True
                print("Putting {0} to defence mode...".format(
                    board[player.number][0][choice].title))
            else:
                print("There is no card there...")

        # Use card effect
        elif move == '10':
            pass
        # Activate a magic card
        elif move == '11':
            pass
        # Discard a card
        elif move == '12':
            print_player_board(board[player.number])

            choice = int(input("(-1 to cancel) Delete card: "))
            if choice == -1:
                continue

            # If it's a magic/trap card set list index to 1
            if choice > 4:
                choice -= 5
                side = 1
            else:
                side = 0

            board[player.number][side][choice] = None


    return player, board

def print_and_get_player_move():
    """Prints all possibel moves and asks for the player's choice."""

    print("""
####################    ###################   #############################
##     Player     ##    ##      Hand     ##   ##         Field           ##
####################    ###################   #############################
-2: Surrender           1: View hand          5: View field
-1: End Turn            2: See card details   6: See card details
0:  Check life points   3: Discard Card       7: Attack with card
                        4: Play Card          8: Sacrifice a card
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
    """Asks player which card they want a detailed description of."""
    print_hand(hand)
    card = int(input("Which card do you want the details of?\nCard: "))
    print
    print_card_details(hand[card])

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

def print_board(board):
    """Prints an ascii representation of a board along with all cards."""
    board_txt = ["","","",""]

    for i, side in enumerate(board):
        for j, type in enumerate(side):
            for card in type:
                if card == None:
                    board_txt[(i * 2) + j] += "[ Nil card ] "
                else:
                    if card.face_down:
                         board_txt[(i * 2) + j] += "[ Facedown ] "
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

def print_player_board(player_board):
    board_txt = ["", ""]
    
    # Generating numbers for user to choose a card
    top_row = bottom_row = ""
    for i in range(5):
        top_row += (" " * 12) + str(i)
        bottom_row += (" " * 12) + str(i + 5)
    

    for j, type in enumerate(player_board):
        for card in type:
            if card == None:
                board_txt[j] += "[ Nil card ] "
            else:
                board_txt[j] += "{0} ".format(card.short_title)

    print("""
{0}
Monst: {1}
Spell: {2}
{3}
""".format(top_row, board_txt[0], board_txt[1], bottom_row))

def print_player_monsters(player_monster_board):
    board_txt = ""

    row_numbers = ""
    for i in range(5):
        row_numbers += (" " * 12) + str(i)

    for card in player_monster_board:
        if card == None:
            board_txt += "[ Nil card ] "
        else:
            board_txt += "{0} ".format(card.short_title)

    print("""
{0}
Monst: {1}
""".format(row_numbers, board_txt))

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

if __name__ == '__main__':
    main()