DECK_SIZE = 52
CARDS = [x for x in xrange(DECK_SIZE)]

def in_shuffle(deck):
    start = 0
    middle = DECK_SIZE / 2

    new_deck = []

    while middle < DECK_SIZE:
        new_deck.append(deck[start])
        new_deck.append(deck[middle])
        start += 1
        middle += 1

    print new_deck
    return new_deck

def out_shuffle(deck):
    start = 0
    middle = DECK_SIZE / 2

    new_deck = []

    while middle < DECK_SIZE:
        new_deck.append(deck[middle])
        new_deck.append(deck[start])
        start += 1
        middle += 1

    print new_deck
    return new_deck