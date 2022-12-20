def exclusion():

    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    y = 2_000_000
    positions = set()
    beacons = set()

    for row in data:
        coordinates = row.split()

        sensor_x = int(coordinates[2].strip("x=,"))
        sensor_y = int(coordinates[3].strip("y=:"))
        beacon_x = int(coordinates[8].strip("x=,"))
        beacon_y = int(coordinates[9].strip("y="))

        if beacon_y == y:
            beacons.add(beacon_x)

        diff_x = abs(sensor_x - beacon_x)
        diff_y = abs(sensor_y - beacon_y)
        diff = diff_x + diff_y

        if y in range(sensor_y - diff, sensor_y + diff + 1, 1):
            offset = diff - abs(sensor_y - y)
            positions.update(range(sensor_x - offset, sensor_x + offset + 1, 1))

    positions -= beacons

    print(f"Positions that cannot contain a beacon: {len(positions)}")

if __name__ == "__main__":

    exclusion()