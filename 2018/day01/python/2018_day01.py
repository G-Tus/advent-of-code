def calibration():

    with open("../input.txt", "r") as file:
          data = file.read().splitlines()

    frequency1 = 0
    frequency2 = 0
    frequencies = {0}
    first = None

    for change in data:
        frequency1 += int(change)

    while True:
        for change in data:
            frequency2 += int(change)
            if not first:
                if frequency2 in frequencies:
                    first = frequency2
                    break

            frequencies.add(frequency2)

        if first:
            break

    print(f"Resulting frequency: {frequency1}")
    print(f"Frequency that appears twice first: {first}")

if __name__ == "__main__":
    calibration()