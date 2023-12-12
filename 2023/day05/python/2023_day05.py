import re

def planting():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    seeds = [int(seed) for seed in re.findall(r"\d+", data[0])]

    mapping = {}

    for line in data[1:]:

        if line == "":
            continue

        elif line[0].isalpha():
            source_target, _ = line.split(" ")
            source, _, target = source_target.split("-")
            mapping[source] = {
                target: []
            }

        elif line[0].isdigit():
            output, start, width = [int(number) for number in line.split(" ")]
            mapping[source][target].append([output, start, width])

    outputs = []

    for seed in seeds:
        source = "seed"

        while True:
            target = list(mapping[source].keys())[0]

            for output, start, width in mapping[source][target]:

                if (seed >= start) and (seed < (start + width)):
                    offset = seed - start
                    seed = output + offset    
                    break

            if target not in mapping:
                break          

            source = target

        outputs.append(seed)

    print(f"Lowest location: {min(outputs)}")

if __name__ == "__main__":
    planting()