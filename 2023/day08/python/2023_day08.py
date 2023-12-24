import re
import math

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

    nodes = []

    for node in network:
        if node[-1] == "A":
            nodes.append(node)

    step = 0

    i = 0

    counts = [[0, 0] for _ in range(len(nodes))]

    while True:
        instruction = 0 if instructions[i] == "L" else 1

        for index, node in enumerate(nodes):
            nodes[index] = network[node][instruction]

        step += 1
        i += 1

        if i >= length:
            i = 0

        z = [(node[-1] == 'Z') for node in nodes]
        if any(z):

            for index, state in enumerate(z):
                if state:
                    counts[index][1] = step - counts[index][0]
                    counts[index][0] = step
            
        if all([(count[1] != 0) for count in counts]):
            break
    
    lcm = math.lcm(*[count[1] for count in counts])
    print(f"Steps required to reach nodes all ending in Z: {lcm}")

if __name__ == "__main__":
    wasteland()