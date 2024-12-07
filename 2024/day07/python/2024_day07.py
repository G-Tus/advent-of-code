from re import findall

def calculator(total, array, intermediate):
    if total < intermediate:
        return 0

    elif len(array) == 1:
        addition = total == intermediate + int(array[0])
        multiplication = total == intermediate * int(array[0])
    
    else:
        number = int(array.pop(0))
        addition = calculator(total, array.copy(), intermediate + number)
        if intermediate == 0: intermediate = 1
        multiplication = calculator(total, array.copy(), intermediate * number)

    return addition or multiplication

def calibration():
    with open("../input.txt", "r") as file:
        data = file.read().splitlines()

    result = 0
    for line in data:
        numbers = findall(r"\d+", line)
        total = int(numbers.pop(0))
        result += total if calculator(total, numbers, 0) else 0
    
    print(f"Total calibration result: {result}")

if __name__ == "__main__":
    calibration()
    