def safe():
    with open("../input.txt", "r") as file:
        input = file.read().splitlines()

    rotation = 50
    total = 0

    for action in input:
        for _ in range(int(action[1:])):
            rotation += -1 if action[0] == "L" else 1

            if rotation > 99:
                rotation = 0

            elif rotation < 0:
                rotation = 99

            if rotation == 0:
                total += 1

    print(f"Total times at rotation 0: {total}")


if __name__ == "__main__":
    safe()
