from collections import Counter


def isNStraightHand(hand, groupSize):
    n = len(hand)
    if n % groupSize != 0:
        return False

    card_count = Counter(hand)

    for card_value in sorted(hand):
        if card_count[card_value]:
            for next_card_val in range(card_value, card_value + groupSize):
                if card_count[next_card_val] == 0:
                    return False
                card_count[next_card_val] -= 1
                if card_count[next_card_val] == 0:
                    card_count.pop(next_card_val)
    return True


if __name__ == '__main__':
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3
    print(isNStraightHand(hand, groupSize))