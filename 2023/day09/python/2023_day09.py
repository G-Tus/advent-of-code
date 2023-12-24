def oasis():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    total = 0

    for line in data:

        values = [int(value) for value in line.split(" ")]
        ends = []

        while True:
            differences = []
            zero = True
            for index, value in enumerate(values[1:]):
                differences.append(value - values[index])

            if all([(value == 0) for value in values]):
                break

            ends.append(value)
            values = differences

        value = 0
        for end in ends[::-1]:
            value += end

        total += value

    print(f"Total of extrapolated values: {total}")
    
if __name__ == "__main__":
    oasis()
            