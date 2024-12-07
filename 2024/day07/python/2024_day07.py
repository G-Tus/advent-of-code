from re import findall

def calculator(total, array, intermediate):
    if total < intermediate:
        return False
    
    number = int(array.pop(0))
    concat = int(str(intermediate) + str(number))

    if not array:
        addition = total == intermediate + number
        multiplication = total == intermediate * number
        concatenation = total == int(str(intermediate) + str(number))
    
    else:
        addition = calculator(total, array.copy(), intermediate + number)
        concatenation = calculator(total, array.copy(), concat)
        if intermediate == 0: intermediate = 1
        multiplication = calculator(total, array.copy(), intermediate * number)

    return addition or multiplication or concatenation

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
    