KEYPAD = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

KEYPAD2 = [
    ["0", "0", "1", "0", "0"],
    ["0", "2", "3", "4", "0"],
    ["5", "6", "7", "8", "9"],
    ["0", "A", "B", "C", "0"],
    ["0", "0", "D", "0", "0"]
]

def bathroom_code(data: list[str], x: int, y: int, keypad: list[list[str]]):
    limit_x = len(keypad[0]) - 1
    limit_y = len(keypad) - 1

    code = ""

    for line in data:
        for move in line:

            match move:
                case "U":
                    y -= 1
                    if y < 0 or keypad[y][x] == "0":
                        y += 1

                case "D":
                    y += 1
                    if y > limit_y or keypad[y][x] == "0":
                        y -= 1

                case "L":
                    x -= 1
                    if x < 0 or keypad[y][x] == "0":
                        x += 1

                case "R":
                    x += 1
                    if x > limit_x or keypad[y][x] == "0":
                        x -= 1

        code += keypad[y][x]

    print(f"Bathroom code: {code}")

if __name__ == "__main__":
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    bathroom_code(data, 1, 1, KEYPAD)
    bathroom_code(data, 0, 2, KEYPAD2)