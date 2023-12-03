def captcha():

    with open("../input.txt", "r") as file:
        data = file.read()

    length = len(data)
    halflength = int(length / 2)
    part1 = 0
    part2 = 0

    for i, current in enumerate(data):
        next1 = data[0 if i == length - 1 else i + 1]
        next2 = data[i - halflength if i >= halflength else i + halflength]

        if current == next1:
            part1 += int(current)

        if current == next2:
            part2 += int(current)
        
    print(f"Solution to captcha part 1: {part1}")
    print(f"Solution to captcha part 2: {part2}")

if __name__ == "__main__":
    captcha()