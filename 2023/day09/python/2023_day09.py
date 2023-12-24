def oasis():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    part1 = 0
    part2 = 0

    for line in data:

        values = [int(value) for value in line.split(" ")]
        ends = []
        begins = []

        while True:
            differences = []
            for index, value in enumerate(values[1:]):
                differences.append(value - values[index])

            if all([(value == 0) for value in values]):
                break

            ends.append(value)
            begins.append(values[0])
            values = differences

        value = 0
        for end in ends[::-1]:
            value += end

        part1 += value

        value = 0
        for begin in begins[::-1]:
            value = begin - value

        part2 += value

    print(f"Total of extrapolated values endings: {part1}")
    print(f"Total of extrapolated values beginnings: {part2}")
    
if __name__ == "__main__":
    oasis()
            