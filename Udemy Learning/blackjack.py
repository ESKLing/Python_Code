import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:

    def __init__(self):
        self.deck = []
        for self.suit in suits:
            for self.rank in ranks:
                self.deck.append(f"{self.rank} of {self.suit}")

    def __str__(self):
        return f"The deck is {self.deck}"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(random.randint(0, len(self.deck) - 1))


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.split()[0]]

        if card.split()[0] == 'Ace':
            self.aces += 1

    def __str__(self):
        return f"{self.cards}. The current value of this hand is {self.value}."


class Account:

    def __init__(self, player='Player', chips=100):
        self.player = player
        self.chips = chips

    def __str__(self):
        self.player = input('Input your name: ')
        return f"Player: {self.player} \nPlayer bank: {self.chips} chips"

    def wins(self, dep_amount):
        self.chips += dep_amount
        print('Winnings added to your chips. Your new total is ' + str(self.chips) + ' chips.')


def player_hand_add():
    game_deck.shuffle()
    player_hand.add_card(game_deck.deal())
    return player_hand


def dealer_hand_add():
    game_deck.shuffle()
    dealer_hand.add_card(game_deck.deal())
    return dealer_hand


def get_player_bet():
    while True:
        player_bet_string = input('Enter your bet: ')
        if player_bet_string.isnumeric():
            break
    return int(player_bet_string)


def bet():
    while True:
        player_bet = get_player_bet()
        if player_bet == 0:
            print('You need to bet an amount of chips.')
        elif player_bet > account.chips:
            print('This bet exceeds your chips. Enter again')
        else:
            account.chips -= player_bet
            print('Bet Accepted.')
            print('You have ' + str(account.chips) + ' chips remaining.')
            return player_bet


def hit():
    hit_or_stand = ''
    while hit_or_stand not in ['HIT', 'STAND', 'H', 'S']:
        hit_or_stand = input('Do you want to hit or stand?: ').upper()
    return hit_or_stand == 'HIT' or hit_or_stand == 'H'


def replay():
    playagain = ''
    while playagain not in ['YES', 'NO', 'Y', 'N']:
        playagain = input("Do you want to play again: Yes or No? ").upper()
    return playagain == 'YES' or playagain == 'Y'


print('Welcome to Blackjack!')
account = Account()
print(account)

while True:
    if account.chips == 0:
        print('You have no more chips to bet with. Thanks for playing.')
        break
    else:
        print('\n')
        game_deck = Deck()
        print('Player bank: ' + str(account.chips) + ' chips')
        p_bet = bet()
        game_play = True
        while game_play:
            player_hand = Hand()
            dealer_hand = Hand()
            [player_hand_add() for i in range(2)]
            print('The current hand of the player is ' + str(player_hand))
            [dealer_hand_add() for i in range(2)]
            print('The current hand of the dealer is [\'' + str(dealer_hand.cards[0] + '\', ?]'))
            player_turn = dealer_turn = True
            while player_turn:
                if player_hand.value == 21:
                    if dealer_hand.value == 21:
                        print('The current hand of the dealer is ' + str(dealer_hand))
                        print('It is a tie!')
                        account.wins(p_bet)
                    else:
                        print('Well done you got 21!')
                        account.wins(p_bet*2)
                    dealer_turn = game_play = False
                    break
                elif player_hand.value > 21:
                    if player_hand.aces:
                        player_hand.value -= player_hand.aces*10
                        print('The hand contains Aces so the value is now ' + str(player_hand.value))
                        player_hand.aces = 0
                        if player_hand.value <= 21:
                            continue
                    print('PLAYER BUSTS!')
                    dealer_turn = game_play = False
                    break
                else:
                    if hit():
                        player_hand_add()
                        print('The current hand of the player is ' + str(player_hand))
                    else:
                        player_turn = False
            while dealer_turn:
                print('The current hand of the dealer is ' + str(dealer_hand))
                if player_hand.value < dealer_hand.value <= 21:
                    print('The dealer beats the player and wins.')
                    game_play = False
                    break
                elif dealer_hand.value > 21:
                    print('Well done you have beat the dealer and won!')
                    account.wins(p_bet*2)
                    game_play = False
                    break
                else:
                    dealer_hand_add()
        if not replay():
            print('Thanks for playing! Your take-home balance is ' + str(account.chips) + ' chips.')
            break