from random import shuffle


class Deck:
    suits = ["spades",
             "hearts",
             "diamonds",
             "clubs"]

    values = ["2", "3",
              "4", "5", "6", "7",
              "8", "9", "10",
              "Jack", "Queen",
              "King", "Ace"]
    remove_card = None

    cards = []

    def __init__(self, values, suits):
        self.values = values
        self.suits = suits

    def __repr__(self):
        return f" {self.cards} "

    def card(self):
        self.cards = []
        for i in self.values:
            for j in self.suits:
                self.cards.append(tuple((i, j)))

    def shuffle(self):
        return shuffle(self.cards)

    def take_card(self, rm):
        self.remove_card = rm
        for i in self.cards:
            if i == rm:
                self.cards.remove(i)


player = Deck(["spades", "hearts", "diamonds", "clubs"],
              ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"])
player.card()
player.shuffle()
player.take_card(("hearts", "Jack"))
print(player)
