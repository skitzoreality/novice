'''
Blackjack card game
text based
Simplified-player vs dealer
single-deck

'''
from random import shuffle
from time import sleep
import os


#1-player place bet
#2-cards dealt
#3-hit or stand
#(ignore insurance, split, double down)
#4-if player not 21 dealer hits till 21 or bust
#special rules-face=10
#            Ace=1 or 11



suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7
          , 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10,'Ace':11}



#Classes
class Card:
    '''initiate card'''
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank+' of '+self.suit

class Deck:
    '''create deck of card, includes shuffleing and dealing deck function'''
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__()
        return 'The deck has:' + deck_comp
    def shuffle(self):
        '''shuffle deck & notify'''
        shuffle(self.deck)
        print('Deck has been shuffled\n')
        sleep(1)
        os.system('clear')
    def deal(self):
        '''issue cards'''
        single_card = self.deck.pop()
        return single_card



class Hand:
    '''values of cards in hand'''
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        '''add cards to hand and calculate total value'''
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    def adjust_for_ace(self):
        '''calculate value for aces included in hand'''
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    '''chip total, bet, win/lose bet'''
    def __init__(self,total=0):
        self.total = total
        self.bet=0
    def win_bet(self):
        '''player won add bet to chip count'''
        self.total += self.bet
    def lose_bet(self):
        '''player loses remove bet from chipcount'''
        self.total -= self.bet
    def take_bet(self):
        '''wager chips before round'''
        while True:
            try:
                self.bet = int(input('How many chips would you like to bet? '))
            except ValueError:
                print('Sorry, a bet must be an integer!')
            else:
                if self.bet > self.total:
                    print("Sorry, your bet can't exceed",self.total)
                else:
                    break


#Functions


def hit(deck,hand):
    '''recieve additional cards'''
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    '''request more cards or not'''
    global PLAYING
    while True:
        choice = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if choice[0].lower() == 'h':
            hit(deck,hand)

        elif choice[0].lower() == 's':
            print(f"{player_one} stands. Dealer is playing.")
            PLAYING = False

        else:
            print("Sorry, please try again.")
            continue
        break


def show_some(player,dealer):
    '''cards on table after deal'''
    os.system('clear')
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print(f"\n{player_one} Hand:", *player.cards, sep='\n ')
    print(f"{player_one}'s Hand =",player.value)

def show_all(player,dealer):
    '''cards on table after reveal'''
    os.system('clear')
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print(f"\n{player_one}'s Hand:", *player.cards, sep='\n ')
    print(f"{player_one}'s Hand =",player.value)


def player_busts(chips):
    '''bust, goes over 21'''
    print(f"{player_one} busts!")
    chips.lose_bet()

def player_21():
    '''player achieves 21'''
    print(f'{player_one} at 21')

def player_wins(chips):
    '''WIN, distribute chips'''
    print(f"{player_one} wins!")
    chips.win_bet()

def dealer_busts(chips):
    '''dealer bust, goes over 21, player wins, distribute chips'''
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(chips):
    '''dealer wins, player loses, remove chips'''
    print("Dealer wins!")
    chips.lose_bet()

def push():
    '''TIE, no change'''
    print(f"Dealer and {player_one} tie! It's a push.")




#Player setup


PLAYING=True
print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until reaching 17. Aces count as 1 or 11.\n\
    We will be playing with one deck. No insurance, splits or double downs.')
player_one=input('\nWhat is your name?')
print('How many chips are you starting with?')
player_chips = Chips(int(input()))


while True:
    #Game/Round setup
    deck = Deck()
    print('\n')
    deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    player_chips.take_bet()
    show_some(player_hand,dealer_hand)
    #Gameplay
    while PLAYING:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_busts(player_chips)
            break
        if player_hand.value==21:
            player_21()
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)
        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_chips)
        else:
            push()
    #Continue or Exit
    print(f"\n{player_one}'s winnings stand at",player_chips.total)
    NEW_GAME=''
    if player_chips.total>0:
        NEW_GAME += input("Would you like to play another hand? Enter 'y' or 'n' ")
    else:
        print('You are out of coins.')
        NEW_GAME+='n'
    if NEW_GAME[0].lower()=='y':
        PLAYING=True
        continue
    print("Thanks for playing!\nGoodbye.")
    sleep(7)
    break
