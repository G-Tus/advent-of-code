def wrapping_paper():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    paper = 0
    ribbon = 0

    for box in data:
        areas = []
        length, width, height = [int(number) for number in box.split("x")]

        areas.append(2 * length * width)
        areas.append(2 * width * height)
        areas.append(2 * height * length)
        areas.append(min(areas) // 2)

        paper += sum(areas)

        ordered = sorted([length, width, height])
        ribbon += 2 * ordered[0] + 2 * ordered[1]
        ribbon += length * width * height

    print(f"Total amount of wrapping paper needed: {paper} square feet")
    print(f"Total length of ribbon needed: {ribbon} feet")

if __name__ == "__main__":
    wrapping_paper()