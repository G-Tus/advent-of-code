def checksum():
    with open("../input.txt", "r") as file:
        data = [[int(number) for number in row.split("\t")] for row in file.read().splitlines()]

    checksum = 0

    for row in data:
        checksum += (max(row) - min(row))

    print(f"Spreadsheet checksum: {checksum}")

if __name__ == "__main__":
    checksum()