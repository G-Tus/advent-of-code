from copy import deepcopy

def keep_away():

    with open("../input.txt", "r") as file:
        lines = file.read().splitlines()

    template = {
        "items": [],
        "operation": None,
        "amount": None,
        "test": 0,
        "true": 0,
        "false": 0,
        "count": 0
    }
    
    modulo = 1
    monkeys = []
    current_monkey = None

    for line in lines:
        split = line.strip().split()
        match split:
            case ["Monkey", number]:
                current_monkey = int(number.strip(":"))
                monkeys.append(deepcopy(template))
            case ["Starting", "items:", *items]:
                monkeys[current_monkey]['items'] = [int(item.strip(",")) for item in items]
            case ["Operation:", *parts]:
                if parts[-1] == "old":
                    monkeys[current_monkey]['operation'] = squared
                elif parts[-2] == "*":
                    monkeys[current_monkey]['operation'] = multiplication
                    monkeys[current_monkey]['amount'] = int(parts[-1])
                else:
                    monkeys[current_monkey]['operation'] = addition
                    monkeys[current_monkey]['amount'] = int(parts[-1])
            case ["Test:", *parts]:
                monkeys[current_monkey]['test'] = int(parts[-1])
                modulo *= monkeys[current_monkey]['test']
            case ["If", *parts]:
                if parts[0] == "true:":
                    monkeys[current_monkey]['true'] = int(parts[-1])
                elif parts[0] == "false:":
                    monkeys[current_monkey]['false'] = int(parts[-1])

    execute_rounds(deepcopy(monkeys), 20, int_div, 3)
    execute_rounds(deepcopy(monkeys), 10000, remainder, modulo)

def execute_rounds(monkeys, rounds, function, number):
    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey['items']:
                monkey["count"] += 1
                new = monkey['operation'](item, monkey['amount'])
                new = function(new, number)
                if new % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(new)
                else:
                    monkeys[monkey['false']]['items'].append(new)
            monkey['items'] = []

    counts = [monkey['count'] for monkey in monkeys]
    counts.sort(reverse=True)

    print(f"Monkey business: {counts[0] * counts[1]}")

def addition(old, amount):
    return old + amount

def multiplication(old, amount):
    return old * amount

def squared(old, amount):
    return old ** 2

def int_div(new, number):
    return new // number

def remainder(new, number):
    return new % number

if __name__ == "__main__":
    keep_away()
