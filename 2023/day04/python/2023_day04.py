import re

def scratchcards():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    total = 0
    counts = {card: 1 for card in range(1, len(data) + 1)}

    for line in data:

        card, numbers = line.split(":")

        card = int(re.search(r"\d+", card).group())

        winning, have = numbers.split("|")

        winning = re.findall(r"\d+", winning)
        have = re.findall(r"\d+", have)

        value = 0
        count = 0
        for number in have:

            if number in winning:
                count += 1
                if value == 0:
                    value = 1
                else:
                    value *= 2

        for i in range(card + 1, card + count + 1):
            counts[i] += counts[card]

        total += value

    print(f"Total points: {total}")
    print(f"Total scratchcards: {sum(counts.values())}")

if __name__ == "__main__":
    scratchcards()