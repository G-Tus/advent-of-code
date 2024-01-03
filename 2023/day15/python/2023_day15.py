def hash_algorithm():

    with open("../input.txt", "r") as file:
        data = file.read().split(",")
    
    
    total = 0

    for sequence in data:
        value = 0

        for character in sequence:
            value += ord(character)
            value *= 17
            value %= 256

        total += value

    print(f"Sum of hash results: {total}")

if __name__ == "__main__":
    hash_algorithm()