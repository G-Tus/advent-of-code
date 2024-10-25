def passwords():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    correct = 0

    for row in data:
        policy, password = row.split(": ")
        min_max, letter = policy.split(" ")
        minimum, maximum = [int(value) for value in min_max.split("-")]

        count = 0

        for character in password:
            if character == letter:
                count += 1

        if count in range(minimum, maximum + 1):
            correct += 1

    print(f"Number of correct passwords: {correct}")

if __name__ == "__main__":
    passwords()