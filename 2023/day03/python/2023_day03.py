import re

def engine():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    rows = len(data) - 1
    columns = len(data[0]) - 1

    part1 = 0
    part2 = 0

    gears = {}

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

                    if data[y][x] == "*":
                        coordinates = f"{x}, {y}"

                        if coordinates not in gears:
                            gears[coordinates] = [amount]
                        else:
                            gears[coordinates].append(amount)

            if re.search(r"[^0-9\.]", adjacent):
                part1 += amount

    for gear in gears.values():

        if len(gear) == 2:
            part2 += gear[0] * gear[1]

    print(f"Engine parts summed: {part1}")
    print(f"Sum of gear ratios: {part2}")

if __name__ == "__main__":
    engine()