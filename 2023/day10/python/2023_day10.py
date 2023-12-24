import re

def maze():

    with open("../input.txt", "r") as file:
        data = file.read()
        start = int(re.search("S", data.replace("\n", "")).start())
        data = data.splitlines()

    width = len(data[0])
    height = len(data)

    y = start // height
    x = start - (y * width)

    dir_x = 0
    dir_y = 0
    
    if data[y - 1][x] in "|F7":
        dir_y = -1
    
    elif data[y][x + 1] in "-7J":
        dir_x = 1

    elif data[y + 1][x] in "|JL":
        dir_y = 1

    elif data[y][x - 1] in "-FL":
        dir_x = -1

    step = 0

    while True:
        x += dir_x
        y += dir_y
        step += 1

        match data[y][x]:
            case "S":
                break

            case "F":
                dir_x = 1 if dir_x == 0 else 0
                dir_y = 1 if dir_y == 0 else 0

            case "7":
                dir_x = -1 if dir_x == 0 else 0
                dir_y = 1 if dir_y == 0 else 0

            case "L":
                dir_x = 1 if dir_x == 0 else 0
                dir_y = -1 if dir_y == 0 else 0

            case "J":
                dir_x = -1 if dir_x == 0 else 0
                dir_y = -1 if dir_x == 0 else 0

            case _:
                continue

    print(f"Steps furthest away from start: {step // 2}")

if __name__ == "__main__":
    maze()