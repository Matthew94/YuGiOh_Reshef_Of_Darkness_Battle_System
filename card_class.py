class CardBase(object):
    def __init__(self, title = "", description = "", card_number = 0,
                 type = ""):
        """Base class for Card. Just has name and description."""
        self.title = title
        self.description = description
        self.card_number = card_number
        self.type = type

class NormalMonsterCard(CardBase):
    def __init__(self, title = "", description = "", card_number = 0,
                 type = "", level = 1, attack = 0, defence = 0,
                 attribute = "", element = ""):
        super(self).__init__(title, description, card_number, type)

        self.level = level

        self.attack = attack
        self.defence = defence

        self.attribute = attribute
        self.element = element

class EffectMonsterCard(object):
    pass

class FusionMonsterCard(object):
    pass

class RitualMonsterCard(object):
    pass

class MagicCard(CardBase):
    pass

class FieldMagicCard(object):
    pass

class TrapCard(CardBase):
    pass

class TokenCard(object):
    pass