HAND_MAP = {
    "5": "A",
    "41": "B",
    "32": "C",
    "311": "D",
    "221": "E",
    "2111": "F",
    "11111": "G"
}

CARD_MAP = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "J": "D",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M"
}

CARD_MAP_2 = {
    "A": "A",
    "K": "B",
    "Q": "C",
    "T": "E",
    "9": "F",
    "8": "G",
    "7": "H",
    "6": "I",
    "5": "J",
    "4": "K",
    "3": "L",
    "2": "M",
    "J": "N"
}

def camel_cards():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    ranking = {}
    ranking_2 = {}

    for game in data:
        hand, bid = game.split(" ")

        hand_type = {}
        rank = ""
        rank_2 = ""
        for card in hand:
            if card not in hand_type:
                hand_type[card] = 1
            else:
                hand_type[card] += 1

            rank += CARD_MAP[card]
            rank_2 += CARD_MAP_2[card]

        hand_value = [str(number) for number in sorted(hand_type.values(), reverse=True)]
        ranking[HAND_MAP["".join(hand_value)] + rank] = int(bid)


        joker = hand_type.pop("J") if "J" in hand_type else 0
        
        if joker != 5:
            hand_value = sorted(hand_type.values(), reverse=True)
            hand_value[0] += joker
            hand_value = [str(number) for number in hand_value]

        else:
            hand_value = ["5"]
        
        ranking_2[HAND_MAP["".join(hand_value)] + rank_2] = int(bid)

    ranking = {hand: ranking[hand] for hand in sorted(ranking, reverse=True)}
    ranking_2 = {hand: ranking_2[hand] for hand in sorted(ranking_2, reverse=True)}

    total = 0
    for i, bid in enumerate(ranking.values(), 1):
        total += (i * bid)

    total_2 = 0
    for i, bid in enumerate(ranking_2.values(), 1):
        total_2 += (i * bid)

    print(f"Total winnings part 1: {total}")
    print(f"Total winnings part 2: {total_2}")

if __name__ == "__main__":
    camel_cards()