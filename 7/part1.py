from enum import Enum
from collections import Counter

with open("input.txt") as file:
    data = file.read().splitlines()


cards_priority = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
}


class CombinationsPriority(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


class Hand:
    def __init__(self, cards: str, bet: int):
        self.cards = cards
        self.bet = bet
        self.combination = self.set_combination()

    def set_combination(self):
        cards_counter = Counter(self.cards)
        cards_count = [value for _, value in cards_counter.items()]
        if 5 in cards_count:
            combination = CombinationsPriority.FIVE_OF_A_KIND.value
        elif 4 in cards_count:
            combination = CombinationsPriority.FOUR_OF_A_KIND.value
        elif 3 in cards_count and 2 in cards_count:
            combination = CombinationsPriority.FULL_HOUSE.value
        elif 3 in cards_count:
            combination = CombinationsPriority.THREE_OF_A_KIND.value
        elif cards_count.count(2) == 2:
            combination = CombinationsPriority.TWO_PAIRS.value
        elif 2 in cards_count:
            combination = CombinationsPriority.ONE_PAIR.value
        else:
            combination = CombinationsPriority.HIGH_CARD.value
        return combination

    def __lt__(self, other):
        for i in range(len(self.cards)):
            if cards_priority[self.cards[i]] == cards_priority[other.cards[i]]:
                continue
            return cards_priority[self.cards[i]] < cards_priority[other.cards[i]]


def play_the_game(hands_by_combination):
    cards_ordered = []
    for combination_hands in hands_by_combination:
        combination_hands.sort()
        cards_ordered.extend(combination_hands)
    return cards_ordered


hands_by_combination = []
for i in range(7):
    hands_by_combination.append([])

for line in data:
    cards, bet = line.split(' ')
    new_hand = Hand(cards, int(bet))
    hands_by_combination[new_hand.combination].append(new_hand)

ordered_cards = play_the_game(hands_by_combination)
result = 0
for key, card in enumerate(ordered_cards):
    result += (key+1) * card.bet
print(result)
