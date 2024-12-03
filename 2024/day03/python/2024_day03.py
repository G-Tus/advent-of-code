from re import findall

def corruption():
    with open("../input.txt", "r") as file:
        data = file.read()
        
    matches = findall(r"mul\((\d+),(\d+)\)", data)

    total = 0

    for match in matches:
        left, right = match
        total += int(left) * int(right)

    print(f"Total of multiplications: {total}")

if __name__ == "__main__":
    corruption()