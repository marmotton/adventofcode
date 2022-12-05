import copy

with open('input') as f:
    raw = f.read().split('\n\n')
    
    start_decks = [[int(x) for x in raw_deck.split() if x.isdigit()] for raw_deck in raw]
    

decks = copy.deepcopy(start_decks)
while len(decks[0]) > 0 and len(decks[1]) > 0:
    # Player 1 wins
    if decks[0][0] > decks[1][0]:
        decks[0].append(decks[0][0])
        decks[0].append(decks[1][0])
    
    # Player 2 wins
    else:
        decks[1].append(decks[1][0])
        decks[1].append(decks[0][0])

    # Remove the cards that have been played
    decks[0].pop(0)
    decks[1].pop(0)

winner_score = 0
for deck in decks:
    for i in range(len(deck)):
        winner_score += deck[i] * (len(deck) - i)

print("Part 1: the winner scored {}".format(winner_score))

# Part 2
decks = copy.deepcopy(start_decks)

def combat(deck1, deck2):
    d1 = deck1.copy()
    d2 = deck2.copy()

    d1_previous = []
    d2_previous = []

    while len(d1) > 0 and len(d2) > 0:
        # Rule 1, player 1 wins if either of the players has the same cards as in a previous round
        if d1 in d1_previous or d2 in d2_previous:
            return {'winner': 1, 'score': 0}
        d1_previous.append(d1.copy())
        d2_previous.append(d2.copy())

        # Each player draws a card
        winner = 0
        card1 = d1.pop(0)
        card2 = d2.pop(0)

        # Play recursive combat if there are enough cards
        if len(d1) >= card1 and len(d2) >= card2:
            winner = combat(d1[:card1], d2[:card2])['winner']
        # Otherwise play normal combat
        else:
            winner = 1 if card1 > card2 else 2

        # The winner takes both cards
        if winner == 1:
            d1.append(card1)
            d1.append(card2)
        else:
            d2.append(card2)
            d2.append(card1)

    # Define winner and score
    if len(d2) == 0:  # Player 1 wins
        winner_deck = d1
        winner = 1
    else:
        winner_deck = d2
        winner = 2

    score = 0
    for i in range(len(winner_deck)):
        score += winner_deck[i] * (len(winner_deck) - i)

    return {'winner': winner, 'score': score}

result = combat(decks[0], decks[1])

print("Part 2: player {} won with score {}".format(result['winner'], result['score']))
