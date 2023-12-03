def cubes():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    part1 = 0
    part2 = 0
    
    for index, line in enumerate(data, 1):
        _, sets = line.split(":")

        possible = True
        maximum = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        for set in sets.split(";"):

            for pair in set.split(","):

                amount, color = pair.strip().split()
                amount = int(amount)

                if amount > limits[color]:
                    possible = False

                if amount > maximum[color]:
                    maximum[color] = amount

        if possible:
            part1 += index

        product = 1
        for number in maximum.values():
            product *= number

        part2 += product

    print(f"Sum of game numbers: {part1}")
    print(f"Sum of powers of sets of cubes: {part2}")

if __name__ == "__main__":
    cubes()