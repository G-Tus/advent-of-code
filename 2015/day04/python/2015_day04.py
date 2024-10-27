from hashlib import md5

def hashing():
    with open("../input.txt", "r") as file:
        secret = file.read()

    number = 0
    part1 = False
    
    while True:
        hashed = md5(f"{secret}{number}".encode()).hexdigest()

        if not part1 and hashed[:5] == "00000":
            print(f"Number for 5 leading zeroes: {number}")
            part1 = True

        if hashed[:6] == "000000":
            print(f"Number for 6 leading zeroes: {number}")
            break
        
        number += 1

if __name__ == "__main__":
    hashing()
