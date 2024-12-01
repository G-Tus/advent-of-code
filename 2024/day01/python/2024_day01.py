def locations():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    left = []
    right = []

    for line in data:
        left_number, right_number = line.split()
        left.append(int(left_number))
        right.append(int(right_number))

    left.sort()
    right.sort()

    difference = [abs(left_number - right_number) for left_number, right_number in zip(left, right)]

    print(f"Total distance between lists: {sum(difference)}")

    similarity = 0

    for left_number in left:
        count = 0

        for right_number in right:
            if left_number < right_number:
                break

            elif left_number == right_number:
                count += 1

        similarity += left_number * count

    print(f"Similarity score: {similarity}")

if __name__ == "__main__":
    locations()