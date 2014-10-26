class Card(object):
    def __init__(self, title = "", description = "", level = 1, attack = 0,
                 defence = 0, attribute = "Normal", type = "Spellcaster",
                 has_effect = False, card_number = 0):
        """Class for an individual card."""
        self.title = title
        self.description = description
        
        self.level = level
        
        self.attack = attack
        self.defence = defence
        
        self.attribute = attribute
        self.type = type
        
        self.has_effect = has_effect