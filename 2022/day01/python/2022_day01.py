def calories():

    with open("../input.txt", 'r') as file:
        lines = file.readlines()

    elf = 1
    elfs = {}

    elfs[f"elf{elf}"] = 0

    for line in lines:
        if line == "\n":
            elf += 1
            elfs[f"elf{elf}"] = 0
            continue

        elfs[f"elf{elf}"] += int(line)

    print(f"Calories of elf with most calories: {max(elfs.values())}")
    sorted_elfs = list(elfs.values())
    sorted_elfs.sort(reverse=True)
    print(f"Calories of top 3 elfs with most calories: {sum(sorted_elfs[:3])}")

if __name__ == "__main__":
    calories()