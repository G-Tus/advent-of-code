from copy import deepcopy

def checksum():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    totals = {
        2: 0,
        3: 0
    }

    other_boxes = deepcopy(data)
    finished = False

    for index, box in enumerate(data):
        counts = {}

        for letter in box:
            if letter not in counts:
                counts[letter] = 1

            else:
                counts[letter] += 1

        values = counts.values()

        if 2 in values:
            totals[2] += 1

        if 3 in values:
            totals[3] += 1

        if finished:
            continue

        other_boxes.pop(index)

        for box2 in other_boxes:
            saved_index = 0
            count = 0
            for i, (left, right) in enumerate(zip(box, box2)):
                if left != right:
                    count += 1
                    saved_index = i

            if count == 1:
                box_id = list(box)
                box_id.pop(saved_index)
                finished = True
                break

    print(f"Checksum of boxes: {totals[2] * totals[3]}")
    print(f"Correct box: {''.join(box_id)}")

if __name__ == "__main__":
    checksum()