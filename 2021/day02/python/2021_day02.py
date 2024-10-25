def submarine():
    with open ("../input.txt", "r") as file:
        data = file.read().splitlines()

    horizontal = 0
    depth = 0

    for movement in data:
        direction, amount = movement.split(" ")
        amount = int(amount)

        match direction:
            case "forward":
                horizontal += amount

            case "down":
                depth += amount

            case "up":
                depth -= amount

    print(f"Final position multiplied: {horizontal * depth}")

if __name__ == "__main__":
    submarine()