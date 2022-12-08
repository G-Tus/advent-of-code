from copy import deepcopy

def supplies():

    with open("../input.txt", 'r') as file:
        data = file.read().splitlines()

    for index, line in enumerate(data):
        if line == "":
            split = index
            break
    
    indexes = []
    stacks = {}
    for index, number in enumerate(data[split - 1]):
        if number != " ":
            indexes.append(index)
            stacks[str(number)] = []

    for line in range(split - 2, -1, -1):
        for stacknumber, index in enumerate(indexes):
            if (item := data[line][index]).isalpha():
                stacks[str(stacknumber + 1)].append(item)

    stacks1 = deepcopy(stacks)
    stacks2 = deepcopy(stacks)

    for instruction in data[split + 1:]:
        amount, source, target = instruction.split(" ")[1::2]
        
        boxes = []

        for _ in range(int(amount)):
            box = stacks1[source].pop()
            stacks1[target].append(box)

            boxes.append(stacks2[source].pop())

        stacks2[target] += boxes[::-1]
            

    answer1 = ""
    answer2 = ""
    for stack in stacks1.values():
        answer1 += stack[-1]

    for stack in stacks2.values():
        answer2 += stack[-1]

    print(f"Top boxes part 1: {answer1}")
    print(f"Top boxes part 2: {answer2}")

if __name__ == "__main__":

    supplies()