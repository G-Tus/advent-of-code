from functools import cmp_to_key

def updates():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    rules = []
    updates = []

    for line in data:
        if "|" in line:
            rule = line.split("|")
            rules.append(rule)

        elif "," in line:
            update = line.split(",")
            updates.append(update)

    lookup = {}

    for left, right in rules:
        if left not in lookup:
            lookup[left] = [right]

        else:
            lookup[left].append(right)

    total = 0
    total_corrected = 0
    compare = lambda left, right: 1 if left in lookup.get(right, []) else -1

    for update in updates:
        corrected = sorted(update, key=cmp_to_key(compare))
        index = len(update) // 2

        if corrected == update:
            total += int(update[index])

        else:
            total_corrected += int(corrected[index])

    print(f"Total of middle pages: {total}")
    print(f"Total of corrected middle pages: {total_corrected}")

if __name__ == "__main__":
    updates()
