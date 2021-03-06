from __future__ import print_function

from card_class import Card
from player_class import Player

from misc_functions import (coin_toss, declare_winner, print_card_details, print_intro_text,
                           discard_excess_from_hand, starting_draw, draw_card)
from print_board_functions import print_board, print_player_board, print_player_monsters
from player_functions import (place_card_on_board, print_and_get_player_move, print_hand, 
                              print_hand_card_details, shuffle_decks)

try:
    input = raw_input
except:
    pass

def main():
    """Program to simulate a battle from Yu-Gi-Oh: Reshef of Destruction.

    players: list of two player objects
    board: list with two lists that each have two lists of 5 slots
    """
    print_intro_text()

    # Setting up players
    players = [Player(0), Player(1)]
    players = shuffle_decks(players)

    # Setting up board: Player 0 Monsters/Magic - Player 1 Monsters/Spells
    board = [[[None] * 5, [None] * 5], [[None] * 5, [None] * 5]]

    starting_draw(players)

    battle_loop(players, board)

    declare_winner(players)



def battle_loop(players, board):
    """Main loop of battle.

    i is an int that can start at 0 or 1 and decides who goes first.
    It's incremented each turn.

    j is i % 2 so it ensures that you can still access the players
    from the lists even after i becomes greater than 1.

    The players draw a card and take their turns until one of them
    hits 0 life points.
    """
    print("\nBattle starting.")

    i = coin_toss()

    while True:
        print("\n##Player {0}'s turn.##".format(players[i].number + 1))
        
        draw_card(players[i])

        players[i], board = do_player_move(players[i], players[i^1], board)

        # Check to see if anyone is at 0 life points
        if not players[0].life_points or not players[1].life_points:
            break

        # Check if the player has too many cards, discard one if over 5
        players[i].hand = discard_excess_from_hand(players[i].hand)

        # TODO: Set all attack mode cards to face up
        
        # Move counter to next turn
        i ^= 1



   
def do_player_move(player, opponent, board):
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

        # View your own field
        elif move == '6':
            print_player_board(board[player.number])

        # See card details
        elif move == '7':
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
        elif move == '8':
            print_player_monsters(board[player.number][0])
            choice = int(input("(-1 to quit)\nChoose a monster to attack with: "))



        # sacrifice a card
        elif move == '9':
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
        elif move == '10':
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
        elif move == '11':
            pass
        # Activate a magic card
        elif move == '12':
            pass
        # Discard a card
        elif move == '13':
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

if __name__ == '__main__':
    main()