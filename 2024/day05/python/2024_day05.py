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

    total = 0
    total_corrected = 0

    for update in updates:
        correct = True
        lookup = {}

        for left, right in rules:
            if left not in update or right not in update:
                continue

            if left not in lookup:
                lookup[left] = [right]

            else:
                lookup[left].append(right)

            for index, page in enumerate(update):
                if left == page:
                    if right in update[:index + 1]:
                        correct = False

        if correct:
            index = len(update) // 2
            total += int(update[index])

        else:
            for number, befores in lookup.items():
                for before in befores:
                    if before in lookup:
                        for extra_before in lookup[before]:
                            if extra_before not in befores:
                                befores.append(extra_before)

            lookup = list(lookup.items())

            for number, befores in lookup:
                i = None

                for index in range(len(update) - 1, -1, -1):
                    page = update[index]
                    if page == number:
                        i = index

                    if page in befores:
                        befores.remove(page)

                    if not befores:
                        j = index
                        break

                if i == None:
                    continue

                switch = update.pop(i)
                update.insert(j, switch)

            index = len(update) // 2
            total_corrected += int(update[index])

    print(f"Total of middle pages: {total}")
    print(f"Total of corrected middle pages: {total_corrected}")

if __name__ == "__main__":
    updates()
