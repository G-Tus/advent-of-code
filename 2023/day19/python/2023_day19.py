import re
from copy import deepcopy

def aplenty():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()
        
    workflows = {}
    parts = []
    categories = "xmas"
    total = 0

    split = False

    for line in data:

        if line == "":
            split = True
            continue

        if not split:
            begin, end = re.finditer(r"[\{\}]", line)

            name = line[:begin.start()]
            instructions = line[begin.end():end.start()]
            instructions = instructions.split(",")

            last = instructions.pop(-1)
            steps = []

            for instruction in instructions:
                step = {}
                check, step["destination"] = instruction.split(":")
                step["letter"] = check[0]
                step["symbol"] = check[1]
                step["number"] = int(check[2:])

                steps.append(step)

            workflows[name] = {
                "steps": steps,
                "last": last
            }

        else:

            part = {}
            values = re.findall(r"\d+", line)

            for category, value in zip(categories, values):
                part[category] = int(value)

            parts.append(part)


    for part in parts:

        name = "in"

        while True:

            workflow = workflows[name]

            name = workflow["last"]

            for step in workflow["steps"]:
                
                if step["symbol"] == "<":

                    if part[step["letter"]] < step["number"]:
                        name = step["destination"]
                        break

                else:

                    if part[step["letter"]] > step["number"]:
                        name = step["destination"]
                        break

            if name == "R":
                break

            if name == "A":
                total += sum(part.values())
                break

    print(f"Total rating of accepted parts: {total}")

    first = {category: {"start": 1, "stop": 4000} for category in categories}
    first["next"] = "in"

    ranges = [first]
    current = None
    total = 0

    while ranges:
        if not current:
            current = ranges.pop(0)

        if current["next"] == "R":
            current = None
            continue

        if current["next"] == "A":
            current.pop("next")

            product = 1
            for width in current.values():
                product *= (width["stop"] - width["start"] + 1)

            total += product
            current = None
            continue

        workflow = workflows[current["next"]]
        current["next"] = workflow["last"]

        for step in workflow["steps"]:

            if step["symbol"] == "<":

                match (current[step["letter"]]["stop"] >= step["number"], current[step["letter"]]["start"] < step["number"]):
                    case (True, True):
                        new = deepcopy(current)
                        new[step["letter"]]["stop"] = step["number"] - 1
                        new["next"] = step["destination"]
                        ranges.append(new)

                        current[step["letter"]]["start"] = step["number"]

                    case (False, True):
                        current["next"] = step["destination"]
                        break

                    case (True, False):
                        continue

            else:

                match (current[step["letter"]]["stop"] > step["number"], current[step["letter"]]["start"] <= step["number"]):
                    case (True, True):
                        new = deepcopy(current)
                        new[step["letter"]]["start"] = step["number"] + 1
                        new["next"] = step["destination"]
                        ranges.append(new)

                        current[step["letter"]]["stop"] = step["number"]

                    case (False, True):
                        continue

                    case (True, False):
                        current["next"] = step["destination"]
                        break

    print(f"Distinct combinations possible: {total}")

if __name__ == "__main__":
    aplenty()