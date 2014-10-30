from random import randint, shuffle

class Player(object):
    def __init__(self):
        self.life_points = 8000
        
        
        
def begin_battle():
    """Program to simulate a battle from Yu-Gi-Oh: Reshef of Destruction."""
    players = [Player(),Player()]
    self.field = [[None] * 5, [None] * 5],
                  [None] * 5, [None] * 5]]
    
    self.hand = [[None] * 5, [None] * 5]
    
    coin_result = coin_toss() 
    
    if coin_result == 1:
        print("Player 1")
    elif coin_result == 0:
        print("Player 2")
    else:
        return

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