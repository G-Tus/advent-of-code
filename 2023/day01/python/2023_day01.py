import re

LUT = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

def trebuchet():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    part1 = 0
    part2 = 0
    
    for line in data:
        digits = re.findall(r"\d{1}", line)
        part1 += int(digits[0] + digits[-1])

        numbers = {}

        for digit in LUT:
            matches = re.finditer(digit, line)
            numbers |= {match.start(): LUT[match.group()] for match in matches}

        sorting = sorted(numbers)

        part2 += int(numbers[sorting[0]] + numbers[sorting[-1]])

    print(f"Answer for part 1: {part1}")
    print(f"Answer for part 2: {part2}")

if __name__ == "__main__":
    trebuchet()