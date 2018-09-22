import random

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
    def __init__(self):  # Don't need any input to create a deck of cards
        # This working depends on Card class existing above
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)  # appends in a sorted order

    def __str__(self):
        total = []
        for card in self.cards:
            total.append(card.__str__())
        # shows up in whatever order the cards are in
        return "\n".join(total)  # returns a multi-line string listing each card

    def pop_card(self, i=-1):
        # removes and returns a card from the Deck
        # default is the last card in the Deck
        return self.cards.pop(i)  # this card is no longer in the deck -- taken off

    def shuffle(self):
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = []  # forming an empty list
        for c in self.cards:  # each card in self.cards (the initial list)
            card_strs.append(c.__str__())  # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs:  # if the string representing this card is not in the list already
            self.cards.append(card)  # append it to the list

    def sort_cards(self):
        # Basically, remake the deck in a sorted way
        # This is assuming you cannot have more than the normal 52 cars in a deck
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)


    def deal(self, total_hands, cards_per_hand):
        player_hand = []
        return_hands = []
        deck = Deck()

        if cards_per_hand != -1:
            for i in range(total_hands):
                for j in range(cards_per_hand):
                    card = deck.pop_card()
                    player_hand.append(card)
                return_hands.append(Hand(player_hand))
                player_hand = [] # reinitialize cards on hand for next player
        else:
            all_card_per_hand = round(len(deck.cards)/total_hands)
            for i in range(total_hands):
                for j in range(all_card_per_hand):
                    card = deck.pop_card()
                    player_hand.append(card)
                return_hands.append(Hand(player_hand))
                # print(len(Hand(player_hand).cards))
                player_hand = [] # reinitialize cards on hand for next player

        return return_hands



class Hand(object):
    # create the Hand with an initial set of cards
    # param: a list of cards
    def __init__(self, init_cards):
        self.cards = []
        for card in init_cards:
            self.cards.append(card)


    # add a card to the hand
    # silently fails if the card is already in the hand
    # param: the card to add
    # returns: nothing
    def add_card(self, card):
        card_str = []

        for hand_card in self.cards:
            card_str.append(hand_card.__str__())

        if card.__str__() not in card_str:
            self.cards.append(card)

    # remove a card from the hand
    # param: the card to remove
    # returns: the card, or None if the card was not in the Hand
    def remove_card(self, card):
        card_str = []

        for hand_card in self.cards:
            card_str.append(hand_card.__str__())

        if card.__str__() in card_str:
            card_index = card_str.index(card.__str__())
            return_card = self.cards.pop(card_index)
            return return_card
        else:
            return None

    # draw a card from a deck and add it to the hand
    # side effect: the deck will be depleted by one card
    # param: the deck from which to draw
    # returns: nothing
    def draw(self, deck):
        drawn_card = deck.pop_card()
        self.add_card(drawn_card)


    def remove_pairs(self):
        new_list = []

        self.cards.sort(key=lambda c: c.rank_num)

        for c in self.cards:
            if new_list and c.rank_num == new_list[-1].rank_num:
                new_list.pop()
            else:
                new_list.append(c)


        self.cards = new_list
