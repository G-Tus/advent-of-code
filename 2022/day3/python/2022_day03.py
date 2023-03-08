def rucksack_items():

    with open("../input.txt", "r") as file:
        rucksacks = file.read().splitlines()
    
    priority = 0
    badge = 0
    lut = {}

    for i in range(1,27):
        lut[chr(i + 96)] = i
        lut[chr(i + 64)] = i + 26
        
    for i, rucksack in enumerate(rucksacks):
        found = [False, False]
        half = int(len(rucksack) / 2)

        for character in rucksack:
            if not found[0] and character in rucksack[half:]:
                found[0] = True
                priority += lut[character]
            
            if (i % 3 == 0) and not found[1] and (character in rucksacks[i + 1]) and (character in rucksacks[i + 2]):
                found[1] = True
                badge += lut[character]

            if all(found):
                break

    print(f"Total priority: {priority}")
    print(f"Total badge priority: {badge}")

if __name__ == "__main__":
    rucksack_items()