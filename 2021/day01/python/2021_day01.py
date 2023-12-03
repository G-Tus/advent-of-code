def depth():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    part1 = 0
    part2 = 0

    previous = int(data[0])

    for current in data[1:]:
        current = int(current)

        if current > previous:
            part1 += 1

        previous = current

    previous = sum([int(number) for number in data[0:3]])

    for index, current in enumerate(data[1:-2], 1):
        current = int(current) + int(data[index + 1]) + int(data[index + 2])

        if current > previous:
            part2 += 1

        previous = current

    print(f"Times depth increased part 1: {part1}")
    print(f"Times depth increased part 2: {part2}")

if __name__ == "__main__":
    depth()