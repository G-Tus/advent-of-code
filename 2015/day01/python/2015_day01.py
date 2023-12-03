def elevator():
    
    with open("../input.txt", "r") as file:
        data = file.read()

    floor = 0
    first = None

    for position, move in enumerate(data, 1):
        if move == "(":
            floor += 1

        elif move == ")":
            floor -= 1

        if not first and floor == -1:
            first = position

    print(f"Santa is on floor: {floor}")
    print(f"Santa first entered basement on postion: {first}")

if __name__ == "__main__":
    elevator()