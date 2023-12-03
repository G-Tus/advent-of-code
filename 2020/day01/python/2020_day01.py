def expenses():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    result = None
    for number1 in data:
        for number2 in data:
            if (int(number1) + int(number2)) == 2020:
                result = int(number1) * int(number2)
                break

        if result:
            break

    print(f"Result: {result}")

if __name__ == "__main__":
    expenses()