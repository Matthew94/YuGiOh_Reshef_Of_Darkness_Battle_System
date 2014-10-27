class CardBase(object):
    def __init__(self, title = "", description = "", card_number = 0):
        """Base class for Card. Just has name and description."""
        self.title = title
        self.description = description
        self.card_number = card_number
        
class NormalMonsterCard(CardBase):
    def __init__(self, title = "", description = "", card_number = 0,
                level = 1, attack = 0, defence = 0, attribute = "", 
                type = ""):
        super(NormalMonsterCard, self).__init__(title, description, 
                                                card_number)
        
        self.level = level
        
        self.attack = attack
        self.defence = defence
        
        self.attribute = attribute
        self.type = type

def EffectMonsterCard(NormalMonsterCard):
    def __init__(self, title = "", description = "", card_number = 0,
                level = 1, attack = 0, defence = 0, attribute = "", 
                type = ""):
        super(NormalMonsterCard, self).__init__(title, description, 
                                                card_number, level, attack,
                                                defence, attribute, type)

def FusionMonsterCard(object):
    pass
    
def RitualMonsterCard(object):
    pass

class MagicCard(CardBase):
    def __init__(self, title = "", description = "", card_number = 0):
        super(NormalMonsterCard, self).__init__(title, description, 
                                                card_number)
                                                
class FieldMagicCard(object):
    pass

class TrapCard(CardBase):
    def __init__(self, title = "", description = "", card_number = 0):
        super(NormalMonsterCard, self).__init__(title, description, 
                                                card_number)
                                                
class TokenCard(object):
    pass