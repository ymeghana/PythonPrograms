from random import shuffle
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 J Q K A'.split()

class Deck:
    def __init__(self):
        print("Creating new order deck!!")
        self.allcards =[(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])

class Hand:
    def __init__(self,cards):
        self.cards=cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self,added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    def __init__(self,name,hand):
        self.name=name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name,drawn_card))
        return drawn_card

    def remove_war_cards(self):
        war_cards =[]
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        """return true if player has cards"""
        return len(self.hand.cards)!=0


print("welcome to war,lets begin")

#create deck obj and split in half
d=Deck()
d.shuffle()
h1,h2 = d.split_in_half()

#create both players
comp = Player("computer",Hand(h1))
name= input("what is your name?")
user = Player(name,Hand(h2))

total_rounds = 0
war_count =0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("time for new round!")
    print("here are the current standings")
    print(user.name+" has the cpount: "+str(len(user.hand.cards)))
    print(comp.name+" has the cpount: "+str(len(comp.hand.cards)))
    print("play a card!!")

    table_cards =[]
    c_cards = comp.play_card()
    p_cards = user.play_card()

    table_cards.append(c_cards)
    table_cards.append(p_cards)

    if c_cards[1] == p_cards[1]:
        war_count += 1

        print("war!!")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        if RANKS.index(c_cards[1]) < RANKS.index(p_cards[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
print("game over, no of rounds:"+str(total_rounds))
print("a war happend "+str(war_count)+" times")
print("Does computer still have cards "+ str(comp.still_has_cards()))
print("Does human still have cards "+ str(comp.still_has_cards()))
