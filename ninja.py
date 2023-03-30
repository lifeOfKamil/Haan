import random


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))

    def return_value(self):
        return self.value


class Deck:
    def __init__(self):
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        for suit in ["♥", "♣", "♦", "♠"]:
            for val in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
                self.cards.append(Card(suit, val))

    def show(self):
        for _ in self.cards:
            _.show()

    def shuffle(self,):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.down = []
        self.up = []

    def draw_hand(self, deck, cards):
        for c in range(cards):
            self.hand.append(deck.draw_card())
        return self

    def draw_cards_up(self, deck, cards):
        for c in range(cards):
            self.up.append(deck.draw_card())
        return self

    def draw_cards_down(self, deck, cards):
        for c in range(cards):
            self.down.append(deck.draw_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()


class Game:
    def get_name(self):
        n = "Enter name for Player: "
        return input(n)

    def compare_lowest(self):
        p1 = "Player 1, what is your lowest card? "
        p1 = input(p1)
        p2 = "Player 2, what is your lowest card? "
        p2 = input(p2)
        if p1 > p2:
            return 0
        else:
            return 1

    def start(self):
        deck = Deck()
        deck.shuffle()

        # Assign Player Names
        player_1 = Player(self.get_name())
        player_2 = Player(self.get_name())

        # Amount of cards facing up / down and draw cards for each player
        cards_on_table = input(
            "How many cards would you like to be face down/face up? ")
        player_1.draw_cards_up(deck, int(cards_on_table))
        player_1.draw_cards_down(deck, int(cards_on_table))
        player_2.draw_cards_up(deck, int(cards_on_table))
        player_2.draw_cards_down(deck, int(cards_on_table))

        # Amount of cards in hand
        cards_in_hand = input(
            "How many cards would you like to have in hand? ")
        player_1.draw_hand(deck, int(cards_in_hand))
        player_2.draw_hand(deck, int(cards_in_hand))

        player_1.show_hand()

        # print(Game.compare_lowest(self))

    def main_game(self):

        pass


game = Game()
game.start()
