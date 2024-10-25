def computer(noun: int, verb: int) -> int:
    with open("../input.txt", "r") as file:
        data = [int(number) for number in file.read().split(",")]

    pointer = 0

    data[1] = noun
    data[2] = verb

    while True:
        match data[pointer]:
            case 1:
                data[data[pointer + 3]] = data[data[pointer + 1]] + data[data[pointer + 2]]
            
            case 2:
                data[data[pointer + 3]] = data[data[pointer + 1]] * data[data[pointer + 2]]

            case 99:
                break

        pointer += 4

    return data[0]

if __name__ == "__main__":
    print(f"Value after running program: {computer(noun=12, verb=2)}")

    finished = False
    for noun in range(100):
        for verb in range(100):
            if computer(noun=noun, verb=verb) == 19690720:
                print(f"Program input: {100 * noun + verb}")
                finished = True
                break

        if finished:
            break
