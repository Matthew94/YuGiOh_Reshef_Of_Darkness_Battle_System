def BattleClass(object):
    def __init__(self):
        type_diffs = {"Wind":"Earth",
                      "Earth":"Thunder",
                      "Thunder":"Water",
                      "Water":"Fire",
                      "Fire":"Forest",
                      "Forest":"Wind":
                      "Shadow":"Light",
                      "Light":"Fiend",
                      "Fiend":"Dream",
                      "Dream":"Shadow"}
    def attack(self, attacker, defender):
        #If type advantage
        if type_diffs[attacker.element] == defender.element:
            damage_result = self.evaluate_damage(attacker, defender)
            self.send_card_to_grave(defender)
        #If type disadvantage
        elif type_diffs[defender.element] == attacker.element:
            pass
        #Else no type clash
        else:
            pass
    def send_card_to_grave(self, card):
        pass
    def evaluate_damage(self, attacker, defender):
        pass
    def update_life_points(self, change, player):
        pass
    