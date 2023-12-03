def fuel():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    total = 0

    for module in data:

        total += int(int(module) / 3) - 2

    print(f"Fuel needed: {total}")

if __name__ == "__main__":
    fuel()