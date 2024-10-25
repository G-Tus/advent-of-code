KEYPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def bathroom_code():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    x = 1
    y = 1
    code = ""

    for line in data:
        for move in line:

            match move:
                case "U":
                    y -= 1
                    if y < 0:
                        y = 0

                case "D":
                    y += 1
                    if y > 2:
                        y = 2

                case "L":
                    x -= 1
                    if x < 0:
                        x = 0
                
                case "R":
                    x += 1
                    if x > 2:
                        x = 2

        code += str(KEYPAD[y][x])

    print(f"Bathroom code: {code}")

if __name__ == "__main__":
    bathroom_code()

