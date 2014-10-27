from YuGiOh_Reshef_Of_Darkness_Battle_System import card_class

def import_cards(card_file):
    deck = []
    cards = {"Normal Monster":card_class.NormalMonsterCard}
    for line in card_file:
        pass