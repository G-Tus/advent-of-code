import re

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

            name = ""

            for step in workflow["steps"]:
                
                if step["symbol"] == "<":

                    if part[step["letter"]] < step["number"]:
                        name = step["destination"]
                        break

                else:

                    if part[step["letter"]] > step["number"]:
                        name = step["destination"]
                        break

            if not name:
                name = workflow["last"]

            if name == "R":
                break

            if name == "A":
                total += sum(part.values())
                break

    print(f"Total rating of accepted parts: {total}")


if __name__ == "__main__":
    aplenty()