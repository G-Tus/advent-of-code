import re

def boatrace():
    
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    durations = [int(number) for number in re.findall(r"\d+", data[0])]
    records = [int(number) for number in re.findall(r"\d+", data[1])]

    total = 1

    for duration, record in zip(durations, records):
        count = 0
        for i in range(0, duration):
            distance = i * (duration - i)

            if distance > record:
                count += 1

        total *= count

    duration = int(re.search(r"\d+", data[0].replace(" ", "")).group())
    record = int(re.search(r"\d+", data[1].replace(" ", "")).group())

    count = 0

    for i in range(0, duration):
        distance = i * (duration - i)

        if distance > record:
            count += 1
        
    print(f"Ways to beat record part 1 multiplied: {total}")
    print(f"Ways to beat record part 2: {count}")

if __name__ == "__main__":
    boatrace()