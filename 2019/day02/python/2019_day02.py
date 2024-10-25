def computer():
    with open("../input.txt", "r") as file:
        data = [int(number) for number in file.read().split(",")]

    pointer = 0

    data[1] = 12
    data[2] = 2

    while True:
        operation = data[pointer]

        match operation:
            case 1:
                data[data[pointer + 3]] = data[data[pointer + 1]] + data[data[pointer + 2]]
            
            case 2:
                data[data[pointer + 3]] = data[data[pointer + 1]] * data[data[pointer + 2]]

            case 99:
                break

        pointer += 4

    print(f"Value after running program: {data[0]}")

if __name__ == "__main__":
    computer()