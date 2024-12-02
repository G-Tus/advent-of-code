def speed():
    with open("../input.txt", "r") as file:
        data = [[int(number) for number in line.split()] for line in file.read().splitlines()]

    safe = 0

    for report in data:
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

        if not difference and (ascending ^ descending):
            safe += 1

    print(f"Amount of safe reports: {safe}")

if __name__ == "__main__":

    speed()