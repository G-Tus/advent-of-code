def elevator():
    
    with open("../input.txt", "r") as file:
        data = file.read()

    floor = 0

    for move in data:
        if move == "(":
            floor += 1

        elif move == ")":
            floor -= 1

    print(f"Santa is on floor: {floor}")

if __name__ == "__main__":
    elevator()