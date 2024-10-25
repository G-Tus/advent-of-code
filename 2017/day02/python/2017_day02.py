from copy import deepcopy

def checksum():
    with open("../input.txt", "r") as file:
        data = [[int(number) for number in row.split("\t")] for row in file.read().splitlines()]

    checksum = 0
    even_checksum = 0

    for row in data:
        checksum += (max(row) - min(row))

        for index, number in enumerate(row):
            divisors = deepcopy(row)
            divisors.pop(index)

            for divisor in divisors:
                if number % divisor == 0:
                    even_checksum += number // divisor

    print(f"Spreadsheet checksum: {checksum}")
    print(f"Spreadsheet even checksum: {even_checksum}")

if __name__ == "__main__":
    checksum()