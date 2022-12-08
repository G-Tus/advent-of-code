def tuning():

    with open("../input.txt", "r") as file:
        data = file.read()

    for index, _ in enumerate(data):
        if len(set(data[index:index + 4])) == 4:
            break
    
    print(f"Start of packet: {index + 4}")

    for index, _ in enumerate(data):
        if len(set(data[index:index + 14])) == 14:
            break

    print(f"Start of message: {index + 14}")

if __name__ == "__main__":

    tuning()