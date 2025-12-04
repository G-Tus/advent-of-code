def safe():
    with open("../input.txt", "r") as file:
        input = file.read().splitlines()

    rotation = 50
    total = 0

    for action in input:
        rotation = (rotation + (-1 if action[0] == "L" else 1) * int(action[1:])) % 100

        if rotation == 0:
            total += 1

    print(f"Total times at rotation 0: {total}")


if __name__ == "__main__":
    safe()
