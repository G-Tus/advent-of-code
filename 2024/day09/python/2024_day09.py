def fragmenter():
    with open("../input.txt", "r") as file:
        data = [int(number) for number in file.read()]

    disk = []
    empty = []
    file = 0
    i = 0

    for index, number in enumerate(data):
        for _ in range(number):
            if (index % 2) == 0:
                disk.append(file)

            else:
                disk.append(None)
                empty.append(i)

            i += 1

        if (index % 2) == 0:
            file += 1

    for index in empty:
        while not (file := disk.pop(-1)): pass

        if index > len(disk):
            disk.append(file)
            break

        disk[index] = file

    checksum = 0
    for index, file in enumerate(disk):
        checksum += file * index

    print(f"Checksum of file disk: {checksum}")

if __name__ == "__main__":
    fragmenter()
