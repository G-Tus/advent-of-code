def rps():

    with open("../input.txt", 'r') as file:
        matches = file.read().splitlines()

    part1 = {
        "A": {
            "X": 4,
            "Y": 8,
            "Z": 3
        },
        "B": {
            "X": 1,
            "Y": 5,
            "Z": 9
        },
        "C": {
            "X": 7,
            "Y": 2,
            "Z": 6
        }
    }

    part2 = {
        "A": {
            "X": 3,
            "Y": 4,
            "Z": 8
        },
        "B": {
            "X": 1,
            "Y": 5,
            "Z": 9
        },
        "C": {
            "X": 2,
            "Y": 6,
            "Z": 7
        }
    }

    score1 = 0
    score2 = 0

    for match in matches:
        you, me = match.split(" ")
        score1 += part1[you][me]
        score2 += part2[you][me]

    print(f"Final score part 1: {score1} points")
    print(f"Final score part 2: {score2} points")


if __name__ == "__main__":
    rps()