import re

def wasteland():
    
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    instructions = data[0]
    length = len(instructions)
    
    network = {}
    for line in data[2:]:
        node, left, right = re.findall(r"[A-Z]+", line)
        network[node] = (left, right)

    node = "AAA"
    step = 0

    i = 0

    while True:
        node = network[node][0 if instructions[i] == "L" else 1]
        step += 1
        i += 1

        if i >= length:
            i = 0

        if node == "ZZZ":
            break

    print(f"Steps required to reach ZZZ: {step}")

if __name__ == "__main__":
    wasteland()