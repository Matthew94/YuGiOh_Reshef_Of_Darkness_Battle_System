from card_class import Card

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