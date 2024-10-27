from copy import deepcopy

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
VOWELS = "aeiou"
PAIRS = ["ab", "cd", "pq", "xy"]

def naughty_strings():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    nice_strings1 = 0
    nice_strings2 = 0

    for string in data:
        vowels = 0
        doubles = False
        pairs = False
        double_pair = False
        split_pair = False

        for letter in string:
            if letter in VOWELS:
                vowels += 1

        for letter in ALPHABET:
            if (2 * letter) in string:
                doubles = True
                break

        for pair in PAIRS:
            if pair in string:
                pairs = True
                break

        for index in range(len(string) - 1):
            string_copy = list(deepcopy(string))
            letters = "".join(string_copy[index:index + 2])
            string_copy[index:index + 2] = "00"

            if letters in "".join(string_copy):
                double_pair = True
                break

        for index in range(len(string) - 2):
            if string[index] == string[index + 2]:
                split_pair = True
                break


        if vowels > 2 and doubles and not pairs:
            nice_strings1 += 1

        if double_pair and split_pair:
            nice_strings2 += 1

    print(f"Amount of nice strings part 1: {nice_strings1}")
    print(f"Amount of nice strings part 2: {nice_strings2}")

if __name__ == "__main__":
    naughty_strings()