import random


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return "Card(" + str(self.value) + "," + str(self.suit) + ")"

    def __getitem__(self, key):
        return self.value

    def show(self):     # prints card
        print("{} of {}".format(self.value, self.suit))

    def return_value(self):   # return value of card
        return self.value


class Deck:
    def __init__(self):
        self.cards = []
        self.generate_deck()

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += " " * i + str(self.cards[i]) + "\n"
        return s

    def generate_deck(self):
        for suit in ["♥", "♣", "♦", "♠"]:
            for val in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
                self.cards.append(Card(suit, val))

    def print_deck(self):    # prints full deck of cards
        for _ in self.cards:
            _.show()

    def value(self):
        for _ in self.cards:
            return Card.return_value(_)

    def is_empty(self):
        return (len(self.cards) == 0)

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.down = []
        self.up = []

    def __getitem__(self, key):
        return self.hand[key]

    def __str__(self):
        for i in range(len(self.hand)):
            return self.hand[i]

    def deal_hand(self, deck, cards):   # deal cards to player
        for c in range(cards):
            self.hand.append(deck.draw_card())
        return self

    def deal_cards_down(self, deck, cards):    # deal cards facing down
        for c in range(cards):
            self.down.append(deck.draw_card())
        return self

    def deal_cards_up(self, deck, cards):   # deal cards facing up
        for c in range(cards):
            self.up.append(deck.draw_card())
        return self

    def show_hand(self):    # prints cards in players hand
        for card in self.hand:
            card.show()

    def play_card(self, card):    # returns card from players hand
        for card in self.hand:
            return self.hand.pop(card)

    # checks if player has no cards left, when cards face down = 0 then done
    def remaining_cards(self):
        if len(self.down) == 0:
            return 0
        else:
            return len(self.down)


class Game:
    def __init__(self):
        card_pile = []

    def get_name(self):    # get name of player
        n = "Enter name for Player: "
        return input(n)

    def compare_lowest(self):   # determines first move of the game, lowest card first
        p1 = "Player 1, what is your lowest card? "
        p1 = input(p1)
        p2 = "Player 2, what is your lowest card? "
        p2 = input(p2)
        if p1 < p2:
            print("Player 1, you start. ")
            return 0
        else:
            print("Player 2, you start. ")
            return 1

    def start(self):    # initializes game, creates and shuffles a deck of cards
        deck = Deck()
        deck.shuffle()

        # Assign Player Names
        player_1 = Player(self.get_name())
        player_2 = Player(self.get_name())

        # Amount of cards facing up / down and draw cards for each player
        cards_on_table = input(
            "How many cards would you like to be face down/face up? ")
        player_1.deal_cards_up(deck, int(cards_on_table))
        player_1.deal_cards_down(deck, int(cards_on_table))
        player_2.deal_cards_up(deck, int(cards_on_table))
        player_2.deal_cards_down(deck, int(cards_on_table))

        # Amount of cards in hand
        cards_in_hand = input(
            "How many cards would you like to have in hand? ")
        player_1.deal_hand(deck, int(cards_in_hand))
        player_2.deal_hand(deck, int(cards_in_hand))

        # player_1.show_hand()
        # player_2.show_hand()
        # print(player_1.__getitem__(3))
        # x = player_1.__getitem__(3)
        # print(x[0])

    def player_turn(self):    # determines which player starts after comparing lowest card
        if self.compare_lowest() == 0:
            self.start_p1()
        else:
            self.start_p2()

    def get_player_card(self):
        pass

    def start_p1(self):
        while Player.remaining_cards() != 0:

            break


game = Game()
game.start()
game.player_turn()
