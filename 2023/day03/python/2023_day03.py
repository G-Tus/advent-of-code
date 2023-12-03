import re

def engine():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    rows = len(data) - 1
    columns = len(data[0]) - 1

    total = 0

    for i, row in enumerate(data):
        numbers = re.finditer("\d+", row)

        for number in numbers:
            start = number.start()
            stop = number.end()
            amount = int(number.group())

            adjacent = ""
            for y in range(max(i - 1, 0), min(i + 1, rows) + 1):
                for x in range(max(start - 1, 0), min(stop, columns) + 1):
                    adjacent += data[y][x]

            if re.search(r"[^0-9\.]", adjacent):
                total += amount

    print(f"Engine parts summed: {total}")

if __name__ == "__main__":
    engine()