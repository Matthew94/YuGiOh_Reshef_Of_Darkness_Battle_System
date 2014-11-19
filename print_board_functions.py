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