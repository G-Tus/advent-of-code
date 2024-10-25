def passwords():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    correct = 0
    correct2 = 0

    for row in data:
        policy, password = row.split(": ")
        numbers, letter = policy.split(" ")
        first, second = [int(value) for value in numbers.split("-")]

        count = 0

        for character in password:
            if character == letter:
                count += 1

        if count in range(first, second + 1):
            correct += 1

        if (password[first - 1] == letter) ^ (password[second - 1] == letter):
            correct2 += 1
 
    print(f"Number of correct passwords part 1: {correct}")
    print(f"Number of correct passwords part 2: {correct2}")

if __name__ == "__main__":
    passwords()