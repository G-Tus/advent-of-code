def depth():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    increased = 0

    previous = int(data[0])

    for current in data[1:]:
        current = int(current)

        if current > previous:
            increased += 1

        previous = current

    print(f"Times depth increased: {increased}")

if __name__ == "__main__":
    depth()