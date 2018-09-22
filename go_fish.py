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