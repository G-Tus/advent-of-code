def expenses():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    part1 = None
    part2 = None

    for number1 in data:
        for number2 in data:
            if (int(number1) + int(number2)) == 2020:
                part1 = int(number1) * int(number2)
            
            for number3 in data:
                if (int(number1) + int(number2) + int(number3)) == 2020:
                    part2 = int(number1) * int(number2) * int(number3)
                    break

            if part1 and part2:
                break

        if part1 and part2:
            break

    print(f"Result part 1: {part1}")
    print(f"Result part 2: {part2}")

if __name__ == "__main__":
    expenses()