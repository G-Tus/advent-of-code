def checksum():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    totals = {
        2: 0,
        3: 0
    }

    for box in data:
        counts = {}

        for letter in box:
            if letter not in counts:
                counts[letter] = 1

            else:
                counts[letter] += 1

        values = counts.values()

        if 2 in values:
            totals[2] += 1

        if 3 in values:
            totals[3] += 1

    print(f"Checksum of boxes: {totals[2] * totals[3]}")

if __name__ == "__main__":
    checksum()