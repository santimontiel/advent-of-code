from typing import Dict, List, Any
from dataclasses import dataclass
from enum import IntEnum
from utils import summary


def read_input(file_name: str) -> List[str]:
    with open(file_name, "r") as f:
        return f.read().splitlines()
    

def card_to_value(card: str, part: int) -> int:
    
    NON_CHARS = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11 if part == 1 else 1,
        "T": 10
    }

    if card.isdigit():
        return int(card)
    return NON_CHARS[card]


class HandTypes(IntEnum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


def hand_analyzer(cards_dict: str, part: int) -> HandTypes:

    # Analyze the card.
    if part == 1:
        if max(cards_dict.values()) == 5:
            hand_type = HandTypes.FIVE_OF_A_KIND
        elif max(cards_dict.values()) == 4:
            hand_type = HandTypes.FOUR_OF_A_KIND
        elif max(cards_dict.values()) == 3 and 2 in cards_dict.values():
            hand_type = HandTypes.FULL_HOUSE
        elif max(cards_dict.values()) == 3:
            hand_type = HandTypes.THREE_OF_A_KIND
        elif sum([v == 2 for v in cards_dict.values()]) == 2:
            hand_type = HandTypes.TWO_PAIR
        elif max(cards_dict.values()) == 2:
            hand_type = HandTypes.ONE_PAIR
        else:
            hand_type = HandTypes.HIGH_CARD

    if part == 2:

        jokers = cards_dict.get(1, 0)
        maximum = 0
        for key, value in cards_dict.items():
            if value > maximum and key != 1:
                maximum = value

        if maximum + jokers == 5:
            hand_type = HandTypes.FIVE_OF_A_KIND
        elif maximum + jokers == 4:
            hand_type = HandTypes.FOUR_OF_A_KIND
        elif max(cards_dict.values()) == 3 and 2 in cards_dict.values():
            hand_type = HandTypes.FULL_HOUSE
        elif sum([v == 2 for v in cards_dict.values()]) == 2 and jokers == 1:
            hand_type = HandTypes.FULL_HOUSE
        elif maximum + jokers == 3:
            hand_type = HandTypes.THREE_OF_A_KIND
        elif sum([v == 2 for v in cards_dict.values()]) == 2 and jokers == 0:
            hand_type = HandTypes.TWO_PAIR
        elif maximum + jokers == 2:
            hand_type = HandTypes.ONE_PAIR
        else:
            hand_type = HandTypes.HIGH_CARD

    return hand_type



@dataclass
class Hand:

    cards_order: List[int]
    bid: int
    hand_type: int

    @classmethod
    def from_instance(cls, line: str, part: int):
        
        cards, bid = line.split(" ")
        
        # Parse the hand.
        cards_dict = dict()
        for char in cards:
            key = card_to_value(char, part)
            if key not in cards_dict:
                cards_dict[key] = cards.count(char)

        # Analyze the hand.
        hand_type = hand_analyzer(cards_dict, part)

        # Carts order.
        cards_order = [card_to_value(char, part) for char in cards]

        return cls(
            bid=int(bid),
            cards_order=cards_order,
            hand_type=hand_type,
        )
    

def custom_sort_reverse_dc(lst: List[HandTypes]) -> List[HandTypes]:
    def custom_key_reverse(element_container: HandTypes) -> tuple:
        return tuple(element_container.cards_order)
    sorted_list = sorted(lst, key=custom_key_reverse)
    return sorted_list


@summary
def part_1(data: List[str]) -> int:

    hands = [Hand.from_instance(line, part=1) for line in data] 

    accum, counter = 0, 1
    for i in range(len(HandTypes)):
        candidates = list(filter(lambda x: x.hand_type == i, hands))
        sorted_candidates = custom_sort_reverse_dc(candidates)
        for c in sorted_candidates:
            accum += c.bid * counter
            counter += 1

    return accum


@summary
def part_2(data: List[str]) -> int:

    hands = [Hand.from_instance(line, part=2) for line in data] 

    accum, counter = 0, 1
    for i in range(len(HandTypes)):
        candidates = list(filter(lambda x: x.hand_type == i, hands))
        sorted_candidates = custom_sort_reverse_dc(candidates)
        for c in sorted_candidates:
            accum += c.bid * counter
            counter += 1

    return accum
   

def main():
    data = read_input("../inputs/day_07.txt")
    part_1(data)
    part_2(data)


if __name__ == "__main__":
    main()