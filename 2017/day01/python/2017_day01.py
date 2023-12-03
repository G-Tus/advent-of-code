def captcha():

    with open("../input.txt", "r") as file:
        data = file.read()

    total = 0

    for i, current in enumerate(data):
        next = data[0 if i == len(data) - 1 else i + 1]

        if current == next:
            total += int(current)
        
    print(f"Solution to captcha: {total}")

if __name__ == "__main__":
    captcha()