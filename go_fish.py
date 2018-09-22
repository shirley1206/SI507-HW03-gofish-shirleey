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
    	
    	while True:
	    	player1_card = input("Player 1, please choose a card: (e.g. Ace of Diamonds)")
	    	if player1.remove_card(player1_card):
	    		break

    	while True:
	    	player2_card = input("Player 2, please choose a card: (e.g. Ace of Diamonds)")
	    	if player2.remove_card(player2_card):
	    		break

	    
	    print('p1 rank_num=', player1_card.rank_num, 'p1 rank_num=', player2_card.rank_num)
	    if not testing:
	        print("Player 1 plays", player1_card, "& Player 2 plays", player2_card)

	        if player1_card.rank_num > player2_card.rank_num:

	            if not testing:
	                print("Player 1 wins a point!")
	            p1_score += 1
	        elif player1_card.rank_num < player2_card.rank_num:
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