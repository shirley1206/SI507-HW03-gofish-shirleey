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


    def deal(self, total_hands, cards_per_hand=7):
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

def play_war_game(testing=False):
    # Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
    deck = Deck()
    deck.shuffle()
    player_hands = deck.deal(2)
    #start a two player game

    p1_score = 0
    p2_score = 0
    player1 = player_hands[0]
    player2 = player_hands[1]


    if not testing:
        print("\n*** BEGIN THE GAME ***\n")


    for play_round in range(7):
        print("Round: " + str(play_round + 1))
        while True:
            print("Player1's current cards:")
            for card in player1.cards:
                print(card)
            player1_card = input("Player 1, please choose a card: (e.g. Ace of Diamonds):") 
            if player1.remove_card(player1_card):
                print("===========Player1 selected a card===========")
                break    
            else:
                print("You don't have this card, try again.")

        while True:
            print("Player2's current cards:")
            for card in player2.cards:
                print(card)
            player2_card = input("Player 2, please choose a card: (e.g. Ace of Diamonds):")
            if player2.remove_card(player2_card):
                print("===========Player2 selected a card===========")
                break
            else:
                print("You don't have this card, try again.")


        # print('p1 rank_num=', player1_card, 'p1 rank_num=', player2_card)
        if not testing:
            print("Player 1 plays", player1_card, "& Player 2 plays", player2_card)
            compare1=player1_card.replace("Ace", "1").replace("Jack", "11").replace("Queen", "12").replace("King", "13").split()
            compare2=player2_card.replace("Ace", "1").replace("Jack", "11").replace("Queen", "12").replace("King", "13").split()
            if int(compare1[0]) > int(compare2[0]):
                if not testing:
                    print("Player 1 wins a point!")
                p1_score += 1
            elif int(compare1[0])< int(compare2[0]):
                if not testing:
                    print("Player 2 wins a point!")
                p2_score += 1
            else:
                if not testing:
                    print("Tie. Next turn.")


    if p1_score > p2_score:
        return "Player1", p1_score, p2_score
    elif p2_score > p1_score:
        return "Player2", p1_score, p2_score
    else:
        return "Tie", p1_score, p2_score


if __name__ == "__main__":
    result = play_war_game()
    print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1], result[2]))
    if result[0] != "Tie":
        print(result[0], "wins")
    else:
        print("TIE!")