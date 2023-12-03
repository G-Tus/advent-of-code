def fuel():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    part1 = 0
    part2 = 0

    for module in data:

        mass = int(int(module) / 3) - 2
        part1 += mass
        part2 += mass

        while True:
            mass = int(int(mass) / 3) - 2
            
            if mass <= 0:
                break

            part2 += mass

    print(f"Fuel needed part 1: {part1}")
    print(f"Fuel needed part 2: {part2}")

if __name__ == "__main__":
    fuel()