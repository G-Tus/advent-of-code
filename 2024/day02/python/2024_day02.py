from copy import deepcopy

def check_safety(report):
    difference = False
    ascending = False
    descending = False

    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]

        if diff < 0:
            ascending = True

        elif diff > 0:
            descending = True

        if abs(diff) > 3 or diff == 0:
            difference = True
            break

    if not difference and (ascending ^ descending):
        return True

    else:
        return False

def reports():
    with open("../input.txt", "r") as file:
        data = [[int(number) for number in line.split()] for line in file.read().splitlines()]

    safe = 0
    fault_safe = 0

    for report in data:
        if check_safety(report):
            safe += 1
            fault_safe += 1
            continue

        for i in range(len(report)):
            new_report = deepcopy(report)
            new_report.pop(i)

            if check_safety(new_report):
                fault_safe += 1
                break

    print(f"Amount of safe reports: {safe}")
    print(f"Amount of safe reports with at most 1 fault: {fault_safe}")

if __name__ == "__main__":
    reports()