def calibration():

    with open("../input.txt", "r") as file:
          data = file.read().splitlines()

    frequency = 0

    for change in data:
        frequency += int(change)

    print(f"Resulting frequency: {frequency}")

if __name__ == "__main__":
    calibration()