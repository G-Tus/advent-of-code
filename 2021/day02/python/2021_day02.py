def submarine():
    with open ("../input.txt", "r") as file:
        data = file.read().splitlines()

    horizontal = 0
    depth = 0
    depth2 = 0
    aim = 0

    for movement in data:
        direction, amount = movement.split(" ")
        amount = int(amount)

        match direction:
            case "forward":
                horizontal += amount
                depth2 += aim * amount

            case "down":
                depth += amount
                aim += amount

            case "up":
                depth -= amount
                aim -= amount

    print(f"Final position multiplied: {horizontal * depth}")
    print(f"Final position with aim multiplied: {horizontal * depth2}")

if __name__ == "__main__":
    submarine()