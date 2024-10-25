def wrapping_paper():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    total = 0

    for box in data:
        areas = []
        length, width, height = [int(number) for number in box.split("x")]

        areas.append(2 * length * width)
        areas.append(2 * width * height)
        areas.append(2 * height * length)
        areas.append(min(areas) // 2)

        total += sum(areas)

    print(f"Total amount of wrapping paper needed: {total}")

if __name__ == "__main__":
    wrapping_paper()