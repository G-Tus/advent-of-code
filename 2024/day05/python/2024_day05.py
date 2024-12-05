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

    for update in updates:
        correct = True

        for index, page in enumerate(update):
            for rule in rules:
                if rule[0] == page:
                    if rule[1] in update[:index + 1]:
                        correct = False
                        break
            
            if not correct:
                break

        if correct:
            index = len(update) // 2
            total += int(update[index])

    print(f"Total of middle pages: {total}")

if __name__ == "__main__":
    updates()
