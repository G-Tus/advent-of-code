def hash_algorithm(sequence):
    value = 0

    for character in sequence:
        value += ord(character)
        value *= 17
        value %= 256

    return value

def lens_library():

    with open("../input.txt", "r") as file:
        data = file.read().split(",")
    
    total = 0
    boxes = [{} for _ in range(256)]

    for sequence in data:
        total += hash_algorithm(sequence)

        if "=" in sequence:
            label, focal = sequence.split("=")
            value = hash_algorithm(label)
            boxes[value][label] = int(focal)

        if "-" in sequence:
            label = sequence[:-1]
            value = hash_algorithm(label)
            boxes[value].pop(label, None)

    power = 0

    for i, box in enumerate(boxes, 1):
        for j, focal in enumerate(box.values(), 1):
            power += i * j * focal

    print(f"Sum of hash results: {total}")
    print(f"Focusing power of resulting lens configuration: {power}")

if __name__ == "__main__":
    lens_library()