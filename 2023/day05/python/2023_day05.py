import re
import time

class Planting:
    def __init__(self):
        self.mapping = {}
        self.planting()

    def seed_location(self, seed):
        source = "seed"
        widths = []
        while True:
            target = list(self.mapping[source].keys())[0]

            for output, start, width in self.mapping[source][target]:
                stop = start + width
                if (seed >= start) and (seed < stop):
                    offset = seed - start
                    widths.append(stop - seed)
                    seed = output + offset    
                    break

            if target not in self.mapping:
                break          

            source = target
            
        return seed, widths
    
    def range_finding(self, start, stop):
        lowest = 0
        while True:
            location, widths = self.seed_location(start)

            if (not lowest) or (location < lowest):
                lowest = location

            start = start + min(widths)

            if start > stop:
                break

        return lowest           

    def planting(self):

        begin = time.perf_counter()

        with open("../input.txt", "r") as file:
            data = file.read().splitlines()

        seeds = [int(seed) for seed in re.findall(r"\d+", data[0])]

        for line in data[1:]:

            if line == "":
                continue

            elif line[0].isalpha():
                source_target, _ = line.split(" ")
                source, _, target = source_target.split("-")
                self.mapping[source] = {
                    target: []
                }

            elif line[0].isdigit():
                output, start, width = [int(number) for number in line.split(" ")]
                self.mapping[source][target].append([output, start, width])

        part1 = 0
        for seed in seeds:
            location, _ = self.seed_location(seed)
            if (not part1) or (location < part1):
                part1 = location

        part2 = 0
        for i in range(0, len(seeds), 2):
            start, length = seeds[i:i + 2]
            stop = start + length
            lowest = self.range_finding(start, stop)
            if (not part2) or (lowest < part2):
                part2 = lowest

        end = time.perf_counter()

        print(f"Lowest location part 1: {part1}")
        print(f"Lowest location part 2: {part2}")
        print(f"Total duration: {end - begin}s")

if __name__ == "__main__":
    Planting()