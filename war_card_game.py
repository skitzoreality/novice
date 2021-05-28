'''
WAR Card game  CPU vs CPU
'''
from random import shuffle
from time import sleep
import pdb

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
             'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank,'of',self.suit
    

class Deck:
    
    def __init__(self):
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        shuffle(self.all_cards)
        sleep(1)
        print('Deck has been shuffled\n')
        
    def deal_one(self):
        return self.all_cards.pop()

class Player:
    
    def __init__(self,name):
        self.name = name
        self.all_cards = [] 
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'{self.name} has {len(self.all_cards)} cards.'

    

player_one = Player(input('Enter first players name\n'))
player_two = Player(input('Enter second players name\n'))

new_deck = Deck()
new_deck.shuffle()

for x in range(int(len(new_deck.all_cards)/2)):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
print('Dealing cards')
sleep(2.5)
print('Cards dealt\n')


game_on = True
round_num = 0
while game_on:
    
    round_num += 1
    sleep(2)
    print(player_one)
    print(player_two)
    sleep(1)
    print(f"\n\nROUND {round_num}\n")
    print("FIGHT!!!\n")
    sleep(1)
    
    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print(f"{player_one.name}  out of cards! Game Over")
        print(f"{player_two.name} WINS!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print(f"{player_two.name} out of cards! Game Over")
        print(f"{player_one.name} WINS!")
        game_on = False
        break
    
    # Otherwise, the game is still on!
    
    # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True

    while at_war:

        print(f'\n{player_one.name} plays')
        sleep(.5)
        print(player_one_cards[-1].rank,'of',player_one_cards[-1].suit)
        sleep(1)
        print(f'\n{player_two.name} plays')
        sleep(.5)
        print(player_two_cards[-1].rank,'of',player_two_cards[-1].suit)
        sleep(1)
        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            print(f'\n{player_one.name} VICTORIOUS!!!\n')
            print((player_one.name),'gains',len(player_two_cards),
                'cards in their deck.')
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            
            # No Longer at "war" , time for next round
            at_war = False
        
        # Player Two Has higher Card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            print(f'\n{player_two.name} VICTORIOUS!!!\n')
            print((player_two.name),'gains',len(player_one_cards),
                'cards in their deck.')
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            # No Longer at "war" , time for next round
            at_war = False

        else:
            sleep(1)
            print('\n\nWAR!!!\n\n')
            sleep(1)
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("\nPlayer One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("\nPlayer Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

    


    
