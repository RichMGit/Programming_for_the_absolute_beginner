import random

card_deck = [2, 2, 2, 2,
             3, 3, 3, 3,
             4, 4, 4, 4,
             5, 5, 5, 5,
             6, 6, 6, 6,
             7, 7, 7, 7,
             8, 8, 8, 8,
             9, 9, 9, 9,
             10, 10, 10, 10,
             11, 11, 11, 11,
             12, 12, 12, 12,
             13, 13, 13, 13,
             14, 14, 14, 14]

players = []
card_pile = []
random.shuffle(card_deck)

class Card:
    def __init__(self, number):
        if not isinstance(number, int) or not 1 < number < 15:
            raise ValueError("Cards must be numbers, between 1 and 15")
        self.number = number

    def string(self):
        l = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        if l[self.number]:
            return l[self.number]
        else:
            return str(self.number)

    def add_to_card_pile(pile, card):
        pile.append(card)

class Pile:

    def __init__(self):
        self.cards = []

    def add(self, card):
        if self._validate(self.cards + [card]):
            self.cards.append(card)
            if card == 10:
                self.wipe()
            return True
        else:
            return False

    def collect(self):
        copy_of_cards = list(self.cards)
        self.wipe()
        return copy_of_cards

    def _wipe(self):
        del self.cards[:]

    def _validate(self, cards):
        last = len(cards) - 1 # index of the last played card
        if last == 0:
            return True
        if cards[last] in [2, 10]:
            return True
        if cards[last - 1] == 7:
            if cards[last] <= cards[last - 1]:
                return True
            elif cards[last] == 10:
                return True
            return False
        if cards[last] >= cards[last - 1]:
            return True
        return False

p = Pile()
p.add(card_to_add)


class Hand:
    def __init__(self):
        self.cards = {'hand': []}

    def add(self, card):
        if card == 10:
            self.cards.append(card)
        else:
            return False

    def remove(self, card):
        self.cards.remove(card)

player1_hand = Hand()
player1_hand.add(11)
player1_hand.remove(11)

class Player:
    def __init__(self):
        self.hand = Hand
        self.facedown

player = Player()
player.hand.add(11)

players = []
for i in range(10):
    players.append(Player())

players[0].hand.add(9)

class Card_Movement:

    def ask_player_for_input(individual, player_input=None):
        if player_input:
            card = player_input
        else:
            card = int(input('Player ' + str(individual + 1) + ', play a card: '))
        return card
cm = Card_Movement()

def print_board(individual):
    h = players[individual]['hand'] # hand []
    u = players[individual]['faceup'] # Faceup []
    d = players[individual]['facedown'] # Facedown []
    print('Player ' + str(individual + 1), 'this is your card deck')
    print('Hand'.ljust(10), end='')
    for i in range(len(h)):
        x = str(h[i])
        print(x.ljust(5), end='')
    print()
    print('Faceup'.ljust(10), end='')
    for i in range(len(u)):
        x = str(u[i])
        print(x.ljust(5), end='')
    print()
    print('Facedown'.ljust(10), end='')
    for i in range(len(d)):
        print('X'.ljust(5), end='')
    print()


def player_turn(i):
    while True:
        print('Pile of cards', card_pile)
        if len(card_pile) > 0:
            print('Last card laid', card_pile[-1])
        print_board(i)
        card_played = cm.ask_player_for_input(i)
        if card_played in players[i]['hand']:
            print()
            if card1.valid_card(card_pile + [card_played]):
                card1.add_to_card_pile(card_pile, card_played)
                hand1.remove_from_hand(i, card_played)
                if len(players[i]['hand']) <= 3:
                    hand1.add_to_hand(i, card_deck)
                print(card_deck)
                if card_played == 10:
                    del card_pile[:]
                    continue
                if card_played in players[i]['hand']:
                    print('do you wish to play this again?, type 0 if not')
                    card_played = cm.ask_player_for_input(i)
                    card1.add_to_card_pile(card_pile, card_played)
                    hand1.remove_from_hand(i, card_played)
                    hand1.add_to_hand(i, card_deck)
                    break
                elif card_played == 0:
                    break
                break
            else:
                print('you cant lay a', card_played, 'on a', card_pile[-1])
        elif card_played == 0:
            print('You cant go')
            players[i]['hand'].extend(card_pile)
            del card_pile[:]
            break
        else:
            print('You do not have that card')

def playing_game():
    while len(card_deck) > 0:
        for player in range(len(players)):
            player_turn(player)



if __name__ == '__main__':
    p = int(input('How many players are playing? 2-4 '))
    for s in range(p):
        players.append({'hand': [], 'facedown': [], 'faceup': []})

    for n in range(3):
        for player in players:
            player['hand'].append(card_deck.pop())
            player['facedown'].append(card_deck.pop())
            player['faceup'].append(card_deck.pop())

playing_game()
