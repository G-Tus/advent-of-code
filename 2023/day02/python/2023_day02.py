def cubes():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    limits = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    total = 0
    for index, line in enumerate(data, 1):
        _, sets = line.split(":")

        possible = True

        for set in sets.split(";"):

            for pair in set.split(","):

                amount, color = pair.strip().split()

                if int(amount) > limits[color]:
                    possible = False
                    break

            if not possible:
                break

        if possible:
            total += index

    print(f"Sum of game numbers: {total}")

if __name__ == "__main__":
    cubes()