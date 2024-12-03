from re import finditer

def corruption():
    with open("../input.txt", "r") as file:
        data = file.read()
        
    multiplications = {match.start(): match.groups() for match in finditer(r"mul\((\d+),(\d+)\)", data)}
    conditionals = {match.start(): match.group() for match in finditer(r"don?'?t?\(\)", data)}
    matches = dict(sorted((multiplications | conditionals).items()))

    active = True
    total = 0
    conditional_total = 0

    for item in matches.values():
        match item:
            case "do()":
                active = True

            case "don't()":
                active = False

            case _:
                left, right = [int(number) for number in item]
                multiplication = left * right
                total += multiplication

                if active:
                    conditional_total += multiplication

    print(f"Total of multiplications: {total}")
    print(f"Total of conditional multiplications: {conditional_total}")

if __name__ == "__main__":
    corruption()